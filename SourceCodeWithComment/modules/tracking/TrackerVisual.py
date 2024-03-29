import cv2
import os
import argparse
import numpy as np
import pandas as pd
#from munkres import munkres
from scipy.optimize import linear_sum_assignment as hungarian
from sklearn.metrics.pairwise import pairwise_distances

### Module imports ###
import sys
sys.path.append('../../')
from common.Track import Track
from modules.detection.BgDetector import BgDetector
from modules.detection.ExtractBackground import BackgroundExtractor
from common.utility import *

class Tracker:
    """
    Class implementation for associating detections into 2D tracklets.        
    """
    
    def __init__(self, dataPath, camId):
        """
        Initialize object
        
        Input:
            dataPath: String path to the video files
            camId: Camera view of the video to be analysed. 1 = Top, 2 = Front
        """
        
        self.cam = camId    # 摄像头ID
        self.loadSettings(dataPath)
        self.tracks = []
        self.trackCount = 0
        self.oldTracks = []


    def loadSettings(self,path):
        """
        Load settings from config file in the provided path.
        
        Config file includes information on the following, which is set in the object:
            ghost_threshold: Threshold for how large the distance cost can be
            
        Input:
            path: String path to the folder where the settings.ini file is located
            camId: Indicates the camera view
        """
        
        config = readConfig(path)
        c = config['Tracker']

        if self.cam == 1:
            self.ghostThreshold = c.getfloat('cam1_ghost_threshold')    # 允许个体间帧间距离
        elif self.cam == 2:
            self.ghostThreshold = c.getfloat('cam2_ghost_threshold')    # 允许个体间帧间距离
        else:
            print("Supplied camera id, {}, is not supported".format(self.cam))
            sys.exit()

        self.maxKillCount = c.getint("max_kill_count")    # 长时间掉帧
        self.minConfidence = c.getfloat("min_confidence")    # 最小置信度
    
    

    def matrixInverse(self, X, lambd = 0.001, verbose=False):    # 矩阵求逆
        """
        Tries to calculate the inverse of the supplied matrix.
        If the supplied matrix is singular it is regularized by the supplied lambda value, which is added to the diagonal of the matrix
        
        Input:
            X: Matrix which has to be inverted
        Output:
            X_inv: Inverted X matrix
        """
        
        try:
            if verbose:
                print("Condition number of {}".format(np.linalg.cond(X)))        
            X_inv = np.linalg.inv(X)
        except np.linalg.LinAlgError as e:
            if 'Singular matrix' in str(e):    # 若是奇异矩阵，则向该矩阵的对角线元素+lambd
                if verbose:
                    print("Adding regularizer of {}".format(lambd))
                    print("Condition number of {}".format(np.linalg.cond(X)))
                X = X + np.diag(np.repeat(lambd,X.shape[1]))    # 对角线元素+lambd
                
                if verbose:
                    print("Condition number of {}".format(np.linalg.cond(X)))
                X_inv = np.linalg.inv(X)    # 求逆
            else:
                raise
        
        return X_inv

    def mahalanobisDistance(self, Xp, Xg, M, psd=False):
        """
        Calcualtes the squared Mahalanobis distance between the supplied probe and gallery images    计算马氏距离的平方
        
        Input:
            Xp: Numpy matrix containg the probe image features, with dimensions [n_probe, n_features]    
            Xg: Numpy matrix containg the gallery image features, with dimensions [n_gallery, n_features]
            M: The Mahalanobis matrix to be used, with dimensions [n_features, n_features]
            psd: Describes whether M is a PSD matrix or not. If True the sklearn pairwise_distances function will be used, while if False a manual implementation is used
            
        Output:
            dm: Outputs a distance matrix of size [n_probe, n_gallery]
        """
        
        if psd:
            return pairwise_distances(Xp, Xg, metric="mahalanobis", VI=M)    # PSD = Positive semi definite，若M是半正定矩阵，则用 sklearn pairwise_distances function计算
        else:    # 若不是半正定矩阵，则用人工方法算
            mA = Xp.shape[0]
            mB = Xg.shape[0]
            dm = np.empty((mA, mB), dtype=np.double)    # probe行 gallery列
            for i in range(0, mA):
                for j in range(0, mB):  
                    difference = Xp[i] - Xg[j]
                    dm[i,j] = difference.dot(M.dot(difference.T))     # 求乘积
            return dm
    


    def pairwiseDistance(self, detections, tracks):    # 计算成对距离
        """
        Calculate pairwise distance between new detections and the old tracks.
        The matrix is of size: [s, s], where s = max(len(detections), len(tracks))*2.
        This is done to allow for potential ghost tracks, so a tracklet is not gone if just a signle detection is missed
        All values are set to a default weight defiend by the ghostThreshold from the config file.
        
        Input:
            detections: List of cv2.Keypoints
            tracks: List of Track objects
        
        Output:
            pDist: Matrix of size [s,s], containing the pairwise distances
        """
        
        maxLen = int(max(len(self.detections),len(self.tracks)))    # detections, tracks 的最大值

        # Init matrix (including ghost tracks)    初始化矩阵（方阵）
        pDist = np.ones((maxLen,maxLen), np.float32)*self.ghostThreshold    #初始化乘上鬼影阈值

        # Update matrix    更新矩阵
        for detIndex in range(len(self.detections)):
            for trackIndex in range(len(self.tracks)):
                pDist[detIndex][trackIndex] = self.distanceFunc(detIndex,trackIndex)    # 计算距离 先检测目标 后轨迹

        return pDist

    
    def distanceFunc(self, detIndex, trackIndex):
        """
        Calculates a cost values between the provided detection and track    计算欧式距离/马氏距离
        
        The Euclidean distance is calculated, and turned into a norm by dividing with the max allwoed distance, from the config file.
        
        Input:
            detIndex: Int index of the detection
            trackIndex: Int index of the track
            
        Output:
            cost: The floating point values cost will either be the distCost or the dissimilarity
        
        """
        
        # Distance cost

        if self.cam == 1:     # 顶视的话，用欧氏距离
            # L2 distance
            distCost = np.linalg.norm(self.tracks[trackIndex].pos[-1]-np.array(self.detections[detIndex].pt))
        elif self.cam == 2:  # Make sure the coordinates are in order x,y and not y,x (as the cov matrix will be incorrect then)
            # Mahalanobis distance    # 侧视的话，用马氏距离
            detPt = np.asarray(self.detections[detIndex].pt).reshape(1,2)    # 关键点的坐标 
            trackPt = np.asarray(self.tracks[trackIndex].pos[-1]).reshape(1,2)    # 轨迹最后一个点的坐标
            mdist = self.mahalanobisDistance(detPt, trackPt, self.tracks[trackIndex].M)  # Square mahalanobis distances

            distCost = np.sqrt(mdist)
        
        return distCost    # 距离（一个数）


    def findMatches(self, assignM):
        """
        Find matches in the matrix computed using Hungarian    用匈牙利算法找匹配
        
        Input:
            assignM: A binary matrix, where 1 indicates an assignment of row n to column m, and otherwise 0    二值矩阵 n行 to m列
                
        Output: 
            matches: List of tuples containing the row and column indecies for the matches    返回匹配的元组
        """

        matches = []
        for mRow in range(0, len(assignM)):
            for pCol in range(0, len(assignM[mRow])):
                if(assignM[mRow][pCol]):
                    matches.append((mRow,pCol))

        matches.sort(key=lambda x: x[1],reverse=True)
        return matches


    def convertBBoxtoList(self, BBdict):
        
        return    [BBdict["tl_x"],
                   BBdict["tl_y"],
                   BBdict["c_x"],                   
                   BBdict["c_y"],                   
                   BBdict["w"],                   
                   BBdict["h"],                   
                   BBdict["theta"],                   
                   BBdict["l_x"],                   
                   BBdict["l_y"],                   
                   BBdict["r_x"],                   
                   BBdict["r_y"],                   
                   BBdict["aa_tl_x"],                   
                   BBdict["aa_tl_y"],                   
                   BBdict["aa_w"],                   
                   BBdict["aa_h"]]

    
    def recognise(self, frameNumber, detections, bbox, verbose=False):
        """
        Update tracker with new measurements.    用每帧检测到的目标更新轨迹
        This is done by calculating a pairwise distance matrix and finding the optimal solution through the Hungarian algorithm.    计算矩阵成对距离，并用最优化算法：匈牙利算法求解
        
        Input: 
            frameNumber: The current frame number (Int)    当前帧号
            detections: List of cv2.keyPoints (the detections) found in the current frame.    当前帧中关键点
            bbox: List of dicts containing bounding boxes associated with the detected keypoints.    bbox数据
            frame: The current frame as numpy array    当前帧号
            labels: Grayscale image where each BLOB has pixel value equal to its label    灰度图 
            verbose: Whether to print information or not.
            
        Output:
            tracks: List of Track objects
        """

        for idx in reversed(range(len(bbox))):    # 过滤置信度低于预设阈值的目标（从后往前）
            if bbox[idx]["confidence"] < self.minConfidence:
                del bbox[idx]
                del detections[idx]

        self.detections = detections

        # Update tracking according to matches
        numNew = len(self.detections)    # 检测数
        numOld = len(self.tracks)    # 轨迹数
        if(verbose):
            print("New detections: ", numNew)
            print("Existing tracks: ", numOld)

        for t in self.tracks:
            if verbose:
                print("ID {} - Kill Count {}".format(t.id, t.killCount))
            t.killCount += 1    # 掉帧数+1
        
        # Construct cost matrix    计算代价矩阵
        costM = self.pairwiseDistance(detections, self.tracks)


        row_ind, col_ind = hungarian(costM)
        matches = [(row_ind[i], col_ind[i]) for i in range(row_ind.shape[0])]
        
        killedTracks = []
        for (mRow, pCol) in matches:    # 遍历每个配对
            ## If the assignment cost is below the Ghost threshold, then update the existing tracklet    如果配对代价低于鬼影阈值，则更新至已有轨迹
            if(costM[mRow][pCol] < self.ghostThreshold):
                # Update existing track with measurement
                p = np.array(detections[mRow].pt)
                self.tracks[pCol].pos.append(p)    #向轨迹坐标点添加
                self.tracks[pCol].bbox.append(self.convertBBoxtoList(bbox[mRow]))    # 把bbox格式转为list 并添加进bbox
                self.tracks[pCol].M = self.matrixInverse(bbox[mRow]["cov"])    # 求协方差矩阵的逆
                self.tracks[pCol].mean = bbox[mRow]["mean"]    # 添加均值
                self.tracks[pCol].frame.append(frameNumber)    # 添加帧号
                self.tracks[pCol].killCount = 0     # 若有更新则killCount置为0
                
            ## If the cost assignment is higher than the ghost threshold, then either create a new track or kill an old one    高于鬼影阈值
            else:
                # A new track is created if the following is true:    会新创建一条track的情况
                # 1) The cost (L2 distance) is higher than the ghost threshold    欧氏距离大于鬼影阈值
                # 2) It is an actual detection (mRow < numNew)   目标号小于检测到的目标数  即配对中的目标是真的，不是dummy detection
                if(mRow < numNew):
                    # Create new track
                    newTrack = Track()
                    p = np.array(detections[mRow].pt)
                    newTrack.pos.append(p)
                    newTrack.bbox.append(self.convertBBoxtoList(bbox[mRow]))
                    newTrack.M = self.matrixInverse(bbox[mRow]["cov"])
                    newTrack.mean = bbox[mRow]["mean"]
                    newTrack.frame.append(frameNumber)
                    newTrack.id = self.trackCount
                    self.trackCount += 1    # id + 1
                    self.tracks.append(newTrack)    # 添加入轨迹集

                    if verbose:
                        print("Num tracks: {}".format(len(self.tracks)))
                
                # The track is deleted if the following is true:    
                # 1) The assigned detection is a dummy detection (mRow >= numNew),    最匹配配对中的目标是填补的 
                # 2) There are more tracks than detections (numOld > numNew)    轨迹数大于检测数
                # 3) The assigned track is a real track (pCol < numOld)    被匹配的轨迹是真的  
                elif(numOld > numNew and pCol < numOld):
                    if(self.tracks[pCol].killCount > self.maxKillCount):    # 是否达到允许错误匹配掉帧上限
                        killedTracks.append(pCol)

                        if verbose:
                            print("Num tracks: {}".format(len(self.tracks)))       
        
        for pCol in sorted(killedTracks, reverse=True):    # 降序
            self.oldTracks.append(self.tracks.pop(pCol))

        del(costM)     
        if verbose:
            print()   
    

###########################
###### MAIN START!!! ######
###########################
def drawline(track,frame): 
    """
    Draw the last 50 points of the provided track on the provided frame
    
    Input: 
        track: Track object
        frame: 3D numpy array of the current frame
        
    Output:
        frame: Input frame with the line drawn onto it
    """
    
    colors = [(255,0,0),
              (255,255,0),
              (255,255,255),
              (0,255,0),
              (0,0,255),
              (255,0,255),
              (0,255,255),
              (100,100,100),
              (100,100,0),
              (0,100,0),
              (0,0,100),
              (100,0,100),
              (0,100,100),
              (150,150,150),
              (150,150,0),
              (150,0,0),
              (0,150,150),
              (0,0,150),
              (150,0,150)]
    # Loop through the positions of the given track
    for idx, i in enumerate(track.pos): 
        # Loop through the 50 newest positions.
        if idx < len(track.pos)-1 and idx < 50:
            line_pos = (int(track.pos[-idx-1][0]),int(track.pos[-idx-1][1]))
            line_pos2 = (int(track.pos[-idx-2][0]),int(track.pos[-idx-2][1]))
            c = colors[track.id%len(colors)]
            cv2.line(frame,line_pos,line_pos2,c,2)
        else:
            break
    return frame
    

def readDetectionCSV(df, downsample):
    kps = []
    bbs = []
    counter = 0
    for i, row in df.iterrows():    # 全部下采样
        bb = {"tl_x": row["tl_x"] / downsample,
              "tl_y": row["tl_y"] / downsample, 
              "c_x": row["c_x"] / downsample,
              "c_y": row["c_y"] / downsample,
              "w": row["w"] / downsample,
              "h": row["h"] / downsample,
              "theta": row["theta"],
              "l_x": row["l_x"] / downsample,
              "l_y": row["l_y"] / downsample,
              "r_x": row["r_x"] / downsample,
              "r_y": row["r_y"] / downsample,
              "aa_tl_x": row["aa_tl_x"] / downsample,
              "aa_tl_y": row["aa_tl_y"] / downsample,
              "aa_w": row["aa_w"] / downsample,
              "aa_h": row["aa_h"] / downsample,
              "label": counter+1
              }
        
        bb["mean"] = np.asarray([row["c_x"] / downsample, row["c_y"] / downsample])
        
        bb["cov"] = np.eye(2)
        if "covar" in row:
            bb["cov"][0,0] = row["var_x"] / (downsample**2)
            bb["cov"][1,1] = row["var_y"] / (downsample**2)
            bb["cov"][0,1] = bb["cov"][1,0] = row["covar"] / (downsample**2)
        
        bb["confidence"] = 1.0
        if "confidence" in row:
            bb["confidence"] = row["confidence"]

        bbs.append(bb)
    
        kps.append(cv2.KeyPoint(float(row["x"] / downsample),float(row["y"] / downsample),1,0,-1,-1,counter+1))
        counter += 1
    
    return kps, bbs

def saveTrackCSV(allTracks, folder, csvFilename, frameCount):
    df = tracks2Dataframe(allTracks)    # 全部上采样
    df['x'] *= det.downsample
    df['y'] *= det.downsample
    df['tl_x'] *= det.downsample
    df['tl_y'] *= det.downsample
    df['c_x'] *= det.downsample
    df['c_y'] *= det.downsample
    df['w'] *= det.downsample
    df['h'] *= det.downsample
    df["aa_tl_x"] *= det.downsample
    df["aa_tl_y"] *= det.downsample
    df["aa_w"] *= det.downsample
    df["aa_h"] *= det.downsample
    df["l_x"] *= det.downsample
    df["l_y"] *= det.downsample
    df["r_x"] *= det.downsample
    df["r_y"] *= det.downsample
    df['cam'] = camId

    outputPath = os.path.join(folder, csvFilename)
    print("Saving data to: {0}".format(outputPath))
    df.to_csv(outputPath)


def videoTracking(path, camId, det, df_fish, video, preDet):    # 视频跟踪
    vidPath = os.path.join(path, 'cam{0}.mp4'.format(camId))
    
    cap = cv2.VideoCapture(vidPath)

    # Close program if video file could not be opened
    if not cap.isOpened():
        print("Could not open video file {0}".format(vidPath))
        sys.exit()


    df_counter = 0
    
    # Prepare tracker
    tra = Tracker(path, camId)       

    frameCount = 0
    while(cap.isOpened()):
        key = cv2.waitKey(1)
        ret, frame = cap.read()
        frameCount += 1
        #print("Frame: {0}".format(frameCount))        
        if key & 0xFF == ord("q"):
            break

        if (ret):

            ## Detect keypoints in the frame, and draw them
            if not preDet or video:    # 若非预检测 
                kps, bbs = det.detect(frame)    
            
            if preDet:    # 若有预检测
                if df_counter >= len(df_fish):
                    break

                fish_row = df_fish.loc[(df_fish['frame'] == frameCount)]    
                if len(fish_row) == 0:
                    continue
                kps, bbs = readDetectionCSV(fish_row, det.downsample)    # 读入CSV
                df_counter += len(fish_row)

            # Associate new detections with tracklets, and potentially create new/kill old tracklets    # 创建或删除轨迹
            tra.recognise(frameCount, kps, bbs)
            
            if video:    # 是否显示
                frame = cv2.drawKeypoints(det.frame, kps, None, (255,0,0), 4)
                t = tra.tracks
                if t is not None:
                    for idx, i in enumerate(t):
                        if i.pos:                        
                            ## Draw line of the tracklet and draw the keypoints again
                            pos = (int(i.pos[len(i.pos)-1][0]),int(i.pos[len(i.pos)-1][1]))
                            frame = drawline(i,frame)    # 画线
                            frame = cv2.drawKeypoints(frame, kps, None, (0,255,0), 4)    # 画点
                
                ## Draw the skeletons        
                frame[(det.thin),0]=0
                frame[(det.thin),1]=0
                frame[(det.thin),2]=255
                cv2.imshow("Frame",frame)

        else:
            if(frameCount > 1000):    #大于1000帧就跳出
                break
            else:
                continue
    
    cap.release()
    cv2.destroyAllWindows()
        
    # Check if /processed/ folder exists
    folder = os.path.join(path,'processed')
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # Save CSV file
    allTracks = tra.tracks+tra.oldTracks
    csvFilename = 'tracklets_2d_cam{0}.csv'.format(camId)
    saveTrackCSV(allTracks, folder, csvFilename, frameCount)


def imageTracking(path, camId, det, df_fish, video, preDet):
    imgPath = os.path.join(path, 'cam{0}'.format(camId))
    
    # Close program if image file could not be opened
    if not os.path.isdir(imgPath):
        print("Could not find image folder {0}".format(imgPath))
        sys.exit()


    df_counter = 0
    
    # Prepare tracker
    tra = Tracker(path, camId)       

    frameCount = 0
    
    filenames = [f for f in sorted(os.listdir(imgPath)) if os.path.splitext(f)[-1] in [".png", ".jpg"]]
    for filename in filenames:
        key = cv2.waitKey(1)
        frame = cv2.imread(os.path.join(imgPath, filename))

        frameCount = int(filename[:-4])
        if key & 0xFF == ord("q"):
            break

        ## Detect keypoints in the frame, and draw them
        if not preDet or video:    #preDet = 0 
            kps, bbs = det.detect(frame)
        
        if preDet:
            if df_counter >= len(df_fish):
                break

            fish_row = df_fish.loc[(df_fish['frame'] == frameCount)]    
            if len(fish_row) == 0:
                continue
            kps, bbs = readDetectionCSV(fish_row, det.downsample)
            df_counter += len(fish_row)

        # Associate new detections with tracklets, and potentially create new/kill old tracklets
        tra.recognise(frameCount, kps, bbs)
        
        if video:
            frame = cv2.drawKeypoints(det.frame, kps, None, (255,0,0), 4)
            t = tra.tracks
            if t is not None:
                for idx, i in enumerate(t):
                    if i.pos:                        
                        ## Draw line of the tracklet and draw the keypoints again
                        pos = (int(i.pos[len(i.pos)-1][0]),int(i.pos[len(i.pos)-1][1]))
                        frame = drawline(i,frame)
                        frame = cv2.drawKeypoints(frame, kps, None, (0,255,0), 4)
            
            ## Draw the skeletons        
            frame[(det.thin),0]=0
            frame[(det.thin),1]=0
            frame[(det.thin),2]=255
            cv2.imshow("Frame",frame)

    # Check if /processed/ folder exists
    folder = os.path.join(path,'processed')
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # Save CSV file
    allTracks = tra.tracks+tra.oldTracks
    csvFilename = 'tracklets_2d_cam{0}.csv'.format(camId)
    saveTrackCSV(allTracks, folder, csvFilename, frameCount)


def csvTracking(path, camId, det, df_fish):
    df_counter = 0
    # Prepare tracker
    tra = Tracker(path, camId)       
    
    frameList = np.linspace(df_fish["frame"].min(), df_fish["frame"].max(), df_fish["frame"].max() - df_fish["frame"].min() + 1, True, dtype=np.int)    # 等差数列

    for frameCount in frameList:
        #print("Frame: {0}".format(frameCount))        
        
        if df_counter >= len(df_fish):
            break
        
        fish_row = df_fish.loc[(df_fish['frame'] == frameCount)]    
        if len(fish_row) == 0:
            continue
        kps, bbs = readDetectionCSV(fish_row, det.downsample)
        df_counter += len(fish_row)

        tra.recognise(frameCount, kps, bbs)

        
    # Check if /processed/ folder exists
    folder = os.path.join(path,'processed')
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # Save CSV file
    allTracks = tra.tracks+tra.oldTracks
    csvFilename = 'tracklets_2d_cam{0}.csv'.format(camId)
    saveTrackCSV(allTracks, folder, csvFilename, frameCount)


if __name__ == "__main__":
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--path", help="Path to folder")
    ap.add_argument("-c", "--camId", help="Camera ID. top = 1 and front = 2")
    ap.add_argument("-v", "--video", action='store_true', help="Show video")
    ap.add_argument("-i", "--images", action='store_true', help="Use extracted images, instead of mp4 file")
    ap.add_argument("-pd", "--preDetector", action='store_true', help="Use pre-computed detections from csv file")
        
    args = vars(ap.parse_args())
    
    # ARGUMENTS *************
    video = args["video"]
    preDet = args["preDetector"]
    useImages = args["images"]

    if args.get("camId", None) is None:
        print('No camera ID given. Exitting.')
        sys.exit()
    else:
        camId = int(args["camId"])
        
    if args.get("path", None) is None:
        print('No path was provided. Try again!')
        sys.exit()
    else:
        path = args["path"]

    df_fish = None
    if preDet:
        detPath = os.path.join(path,'processed', 'detections_2d_cam{0}.csv'.format(camId))
        if os.path.isfile(detPath):
            df_fish = pd.read_csv(detPath, sep=",") 
        else:
            print("Detections file found '{}' not found. Ending program".format(detPath))
            sys.exit()


    bgPath = os.path.join(path, 'background_cam{0}.png'.format(camId))

    # Check if background-image exists
    if not os.path.isfile(bgPath):
        print("No background image present") 
        print("... creating one.") 
        bgExt = BackgroundExtractor(path, camId, video = not useImages)
        bgExt.collectSamples()
        bg = bgExt.createBackground()
        cv2.imwrite(bgPath, bg)

    # Prepare detector
    det = BgDetector(camId, path)

    if preDet:
        csvTracking(path, camId, det, df_fish)
    else:    # preDet = 0
        if useImages:
            imageTracking(path, camId, det, df_fish, video, preDet)
        else:
            videoTracking(path, camId, det, df_fish, video, preDet)
