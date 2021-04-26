import numpy as np
import pandas as pd
import argparse
import os.path
import configparser
import networkx as nx
import cv2
import scipy.stats
### Module imports ###
import sys
sys.path.append('../../')
from common.utility import csv2Tracks,readConfig, getDropIndecies, prepareCams
from common.Track import Track
from modules.reconstruction.Triangulate import Triangulate


class TrackletMatcher:    # 2D -> 3D
    """
    Class implementation for associating 2D tracklets into 3D tracklets        
    """
    
    def __init__(self, dataPath):
        """
        Initialize object
        
        Input:
            dataPath: String path to the main folder
        """
        
        # Load settings and data
        self.loadSettings(dataPath)
        self.loadTracklets(dataPath)
        self.cams = prepareCams(dataPath) # Load camera objects  输入相机pkl文件路径

        # Internal stuff
        self.graph = nx.DiGraph()
        self.camIdMap = {}
        self.triangulated = {}


    def loadSettings(self,path):    # 读入配置内容：
        
        """
        Load settings from config file in the provided path.
        
        Config file includes information on the following, which is set in the object:
            reprojection_err_mean: The mean value of a Gaussian distribution of reprojection errors    重投影的平均差
            reprojection_err_std: The standard deviation of a Gaussian distribution of reprojection errors    重投影的标准差
            movement_err_mean: The mean value of a Gaussian distribution of movement errors    移动的平均差
            movement_err_std: The standard deviation of a Gaussian distribution of movement errors    移动的标准差    
            same_view_max_overlap: The maximum allowed frame overlap of two tracklets    允许两跟踪轨迹交叠  
            tracklet_min_length: Minimum tracklet length    轨迹的最小长度    
            camera_1_sync_frame: Sync frame for camera 1    摄像头1的同步帧
            camera_2_sync_frame: Sync frame for camera 2    摄像头2的同步帧
            
        Input:
            path: String path to the folder where the settings.ini file is located
        """
        
        config = readConfig(path)
        
        # Get tracklet matching parameters
        c = config['TrackletMatcher']
        self.reprojMeanErr = c.getfloat('reprojection_err_mean')    
        self.reprojStdErr = c.getfloat('reprojection_err_std')
        self.movErrMean = c.getfloat('movement_err_mean')
        self.movErrStd = c.getfloat('movement_err_std')  
        self.sameViewMaxOverlap = c.getint('same_view_max_overlap')
        self.trackletMinLength = c.getint('tracklet_min_length')
        self.temporalPenalty = c.getint('temporal_penalty')
        self.FPS = c.getint('FPS')
        self.camera2_useHead = c.getboolean("cam2_head_detector", False)    # 是否使用的是FASTER R-CNN Head

        # Get aquarium size
        c = config['Aquarium']
        self.maxX = c.getfloat("aquarium_width")    # 鱼缸的宽
        self.maxY = c.getfloat("aquarium_depth")    # 鱼缸的长
        self.maxZ = c.getfloat("aquarium_height", np.inf)
        
        self.minX = c.getfloat("min_aquarium_width", 0.0)
        self.minY = c.getfloat("min_aquarium_depth", 0.0)
        self.minZ = c.getfloat("min_aquarium_height", 0.0)

        print("Aquarium Dimensions\n\tX: {} - {}\n\tY: {} - {}\n\tZ: {} - {}\n".format(self.minX, self.maxX, self.minY, self.maxY, self.minZ, self.maxZ))

        # Get camera synchronization parameters
        c = config['CameraSynchronization']
        cam1frame = c.getint('cam1_sync_frame')
        cam2frame = c.getint('cam2_sync_frame')
        self.camera1_offset = max(0,cam2frame-cam1frame)
        self.camera2_offset = max(0,cam1frame-cam2frame)       
        self.camera1_length = c.getint("cam1_length")
        self.camera2_length = c.getint("cam2_length")        


    def loadTracklets(self,path):    # 读入2D轨迹
        """
        Loads the 2D tracklets extracted by TrackerVisual.py
        The tracklets are loaded as dicts, where the key is a combination of the tracklet ID and camera ID
        
        Input:
            path: String path the main folder, containing the processed folder with the 2D tracklets.   
        """
        
        self.cam1Tracks = csv2Tracks(os.path.join(path, 'processed/tracklets_2d_cam1.csv'),
                                     offset=self.camera1_offset,
                                     minLen=self.trackletMinLength,
                                     maxFrame=self.camera1_length)    # 读入摄像头1的轨迹
        self.cam2Tracks = csv2Tracks(os.path.join(path,'processed/tracklets_2d_cam2.csv'),
                                     offset=self.camera2_offset,
                                     minLen=self.trackletMinLength,
                                     maxFrame=self.camera2_length)    # 读入摄像头2的轨迹 

        cam1Info = "Camera 1\n\tLength: {}\n\tOffset: {}\n\tUnique IDs: {}".format(self.camera1_length, self.camera1_offset, len(self.cam1Tracks))    # 打印摄像头1视频的长度、偏移和轨迹条数
        cam2Info = "Camera 2\n\tLength: {}\n\tOffset: {}\n\tUnique IDs: {}".format(self.camera2_length, self.camera2_offset, len(self.cam2Tracks))    # 打印摄像头2视频的长度、偏移和轨迹条数
        print(cam1Info)
        print(cam2Info)
        
            

    def withinAquarium(self,x,y,z):    # 判断座标点是否在鱼缸内
        """
        Checks whether the provided x,y,z coordinates are inside the aquarium.
        
        Input:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        
        Output:
            Boolean value stating whether the point is inside the aquarium
        """

        if(x < self.minX or x > self.maxX):
            return False
        if(y < self.minY or y > self.maxY):
            return False
        if(z < self.minZ or z > self.maxZ):
            return False
        return True


    def findConcurrent(self,track,candidates):    # 求一个轨迹实例内的帧号至另外一个视角全部轨迹的各自帧号有相同帧号的轨迹（返回有着共同帧号的轨迹对象）
        """
        Finds the concurrent tracks (i.e. within the same span of frames) between a specific track and a set of  othertracks 
        
        Input:
            track: A Track object    # 一个轨迹实例
            candidates: List of Track objects    # 列表内是多个轨迹实例
            
        Output:
            concurrent: List of Track objects from candidates that were concurrent with the track argument
        """
        
        concurrent = []
        for c in candidates:
            frames = np.intersect1d(track.frame, candidates[c].frame)    # 求交集
            if(len(frames) == 0):    # 无交集
                continue        
            concurrent.append(candidates[c])
        return concurrent


    def calcMatchWeight(self,track1,track2):    #从两个视角计算两轨迹之间的权重
        """
        Calculate the weight between two tracks from different views.
        The weight is a weighted median value of the inverse CDF value of the reprojection errors between the two tracks.    这个权重是 两轨迹 重投影差值的逆累积分布函数值 的加权中位数
        The Gaussian CDF is used, with parameters loaded in the config file, and it is inverted so value below the mean (i.e. towards 0) is trusted more than value above
        
        Input:
            track1: Track obejct from the top camera
            track2: Track object from the front camera
            
        Output:
            weight: Weight of the constructed 3D tracklet
            track3d: Track object containing the 3D tracklet
        """
        
        frames = np.intersect1d(track1.frame, track2.frame)    # 求轨迹1和轨迹2的交集

        # Prepare new 3d track for saving triangulated information    准备存入3D轨迹的三角信息
        track3d = Track()
        track3d.errors = []
        track3d.reproj = []
        track3d.positions3d = []
        track3d.cam1reprojections = []
        track3d.cam2reprojections = []
        track3d.cam1positions = []
        track3d.cam2positions = []
        track3d.cam1bbox = []
        track3d.cam2bbox = []
        track3d.cam1frame = []
        track3d.cam2frame = []
        track3d.cam1Parent = track1    # 存入cam1的2D轨迹实例
        track3d.cam2Parent = track2    # 存入cam2的2D轨迹实例
        
        frameList = []
        
        for f in sorted(frames):      # 默认升序
            ## Reproject the tracks
            err,pos3d,cam1reproj,cam2reproj,cam2Pt = self.calcReprojError(f,track1,track2)
            track3d.reproj.append(err)

            ## Get the weight as the inverted CDF value.    逆累积分布函数
            err = 1-scipy.stats.expon.cdf(err, scale=self.reprojMeanErr)    # reprojMeanErr为重投影均差，指数分数分布内的lambda
            
            if(self.withinAquarium(*pos3d)):    # 点是否在鱼缸
                track3d.errors.append(err)
            else:
                continue
                
            track3d.positions3d.append(pos3d) 
            track3d.cam1reprojections.append(cam1reproj)    # 顶视重投影的坐标
            track3d.cam2reprojections.append(cam2reproj)    # 侧视重投影的坐标
            track3d.cam1positions.append(track1.getImagePos(f))    # 顶视的源坐标
            track3d.cam2positions.append(track2.getImagePos(f, cam2Pt))   # 侧视的源坐标  
            track3d.cam1bbox.append(track1.getBoundingBox(f))
            track3d.cam2bbox.append(track2.getBoundingBox(f))
            track3d.cam1frame.append(track1.getVideoFrame(f))
            track3d.cam2frame.append(track2.getVideoFrame(f))
            frameList.append(f)    # 筛选掉推测点不在鱼缸内的frame
            
        if len(track3d.errors) > 0:
            track3d.frame = np.array(frameList)      # track3d.frame 为 交集的帧号集
            weight = np.median(track3d.errors) * (len(track3d.errors)/len(list(np.union1d(track1.frame, track2.frame))))    # 权重= errors的中位数 * (errors的长度/t1帧数 ∩ t2帧数）
            return weight,track3d    
        else:
            return 0, None
    
    
    def calcReprojError(self,frameNumber,track1,track2, verbose=False):    # 计算重投影误差
        """
        Calculates the reprojection error between the provided tracklets at the specified frame
        This is done using a Triangulate object.
        
        Input:
            frameNumber: Index of the frame to be analyzed    用来计算重投影误差的帧号
            track1: Track obejct containing the first tracklet    轨迹一
            track2: Track object containing the second tracklet    轨迹二
            
        Output:
            err: Reprojection error (Euclidean distance) between the actual points of the tracks, and the reprojected points    用欧氏距离作为重投影误差
            p: 3D position of the 3D tracklet      轨迹中的3D坐标点
            p1: 2D point of p reprojected onto camera view 1    重投影得到的3D坐标点在视角1的2D坐标
            p2: 2D point of p reprojected onto camera view 2    重投影得到的3D坐标点在视角2的2D坐标
        """
        minErr = np.inf    # 无穷
        minP = None
        minP1 = None
        minP2 = None
        minPt = None

        cam2_list = ["l","c","r"]    # 传统有三个点
        if self.camera2_useHead: 
            cam2_list = ["kpt"]    # FASTER R-CNN-H 只有一个点

        for pt in cam2_list:    # 若传统，三个点选error最小的点，若FASTER R-CNN-H，则只有一个点
            tr = Triangulate()
        
            t1Pt = track1.getImagePos(frameNumber, "kpt")
            t2Pt = track2.getImagePos(frameNumber, pt)
            
    
            # 1) Triangulate 3D point
            p,d = tr.triangulatePoint(t1Pt,
                                      t2Pt,
                                      self.cams[track1.cam],
                                      self.cams[track2.cam],
                                      correctRefraction=True)    # 考虑介质不同的折射
        
            p1 = self.cams[track1.cam].forwardprojectPoint(*p)
            p2 = self.cams[track2.cam].forwardprojectPoint(*p)
    
            # 2) Calc re-projection errors
            pos1 = np.array(t1Pt)
            err1 = np.linalg.norm(pos1-p1)
            pos2 = np.array(t2Pt)
            err2 = np.linalg.norm(pos2-p2)
            err = err1 + err2     # 两视角的重投影误差和
            
            if err < minErr:    # 计算在 "kpt" / "l""c""r" 模式的最小误差的点
                minErr = err
                minP = p
                minP1 = p1
                minP2 = p2
                minPt = pt    # "kpt" / "l""c""r"
            
        if verbose:
            print("Min error: {}\n\t3D coords: {}\n\tTrack 1: {}\n\tTrack 2: {}\n\tPos1 {} (GT) / {}\n\tPos2 {} (GT) / {}\n\tTrack 2 pt: {}".format(minErr, minP, track1.id, track2.id, pos1, p1, pos2, p2, minPt))
        return minErr, minP, minP1, minP2, minPt


    def createNodes(self, verbose=False):
        """
        Populates the internal graph with nodes, where each node is a 3D tracklet with the weight from calcMatchWeight    用节点填充图，每个节点都是带有权重的轨迹点
        Only 2D tracklets which are concurrent are analyzed.    只有两个视角都有轨迹的帧才会被添加
        
        Also stores all the 3D tracklets in a internal triagnualted structure
        
        Input:
            Verbose: Whether to print information for each node added
        """
        
        for tId in self.cam1Tracks:    # 取顶视内的一个轨迹实例
            t = self.cam1Tracks[tId]
            concurrent = self.findConcurrent(t,self.cam2Tracks)    # 求与该顶视轨迹 有交集的侧视轨迹实例集
            
            for c in concurrent:    # c 是每个track
                weight,track3d = self.calcMatchWeight(t,c)    # 计算该顶视轨迹 与侧视轨迹交集 的权重  误差越大，权值越小
                if(weight <= 0.001) or track3d is None:    # 若权重小于0.001 或 track3d 为空，则不创建结点
                  continue
                nodeName = "{0}-{1}".format(t.id,c.id)    # 轨迹名为 "{0}-{1}".format(t.id,c.id)
                self.graph.add_node(nodeName, weight=weight,    # 结点的信息有： 结点名，权重，帧号，cam1中的id，cam2中的id
                                    frames=track3d.frame,
                                    cam1=t.id,
                                    cam2=c.id)
                self.addToMap(nodeName)    # 加入到Map中，键为id，值为nodeName

                # Save triangulated information    3d 实例保存到字典内，键为nodeName，值为3d轨迹实例
                self.triangulated[nodeName] = track3d
                
                if verbose:
                    print("Added node:")
                    print(" {0}-{1} with weight: {2}".format(t.id, c.id, weight))


    def addToMap(self, nodeName):
        """
        Populates the internal camera id map, which is a dict tracking that per 2D tracklet writes all 'nodeNames' (i.e. identifiers for nodes in the internal graph)
        that the 2D tracklet is a part of.
        
        Input:
            nodeName: A string signifying the 2 2D tracklets used for a 3D tracklet
        """
        
        for key in ['cam1','cam2']:
            currId = self.graph.nodes[nodeName][key]    # 取得该结点 cam1/2的id
            if(currId not in self.camIdMap):    # 若该id不在camIdMap内，则新建键值
                self.camIdMap[currId] = []
            self.camIdMap[currId].append(nodeName)    # 向camIdMap字典，键为该id的值中添加入nodeName


    def connectNodes3D(self, verbose=False):    # 连接结点
            """
            Per tracklet goes through and calculates an edge weight between all nodes with the same trackID in its node name    每个id相同的轨迹遍历算出各个结点之间带权边
            This is an attempt to combine tracklets in a view, who is associated with the same tracklet in the other view.
            This way tracklets in the same view can be associated, even though there are frames missing in between
            
            This is done if based on te average speed to travel between the two 2D tracklet positions of which is not hte same trackle
            The edge weight is based on the inverse CDF value of the distance between the first and last frames in the 2D tracklets in the same view.
            The CDF value is multiplied with the sum of the node weights for the 2 nodes being connected.
            
            Input:
                verbose: Whether to print information on the nodes connected and their weights.
            """

            for trackId in self.camIdMap:     # 遍历camIdMap字典 其中 键为id，值为nodeName
                elements = [e for e in self.camIdMap[trackId]]     # 键为id，值为nodeName，即取得所有nodeNmae
                    
                for e1 in elements:    # 遍历每个nodeName   两两遍历
                    e1Track = self.triangulated[e1]   # 取一个3D 轨迹实例
                    
                    for e2 in elements:    # 遍历每个nodeName
                        if(e1 == e2):    # 若相同则跳过
                            continue
                        e2Track = self.triangulated[e2]    # 取另一个3D 轨迹实例
                        
                        frameDiff = e2Track.frame[0]-e1Track.frame[-1]    # 求 e1最后一帧 至 e2第一帧的时间距离
                        posDiff = np.linalg.norm(e1Track.positions3d[-1]-e2Track.positions3d[0])    # 求 e1最后一帧坐标 至 e2第一帧坐标 空间距离

                        overlap3D = (e2Track.frame[0]-e1Track.frame[-1]) <= 0    # overlap3D 为3D重叠标志位
                        
                        overlap2D = False    # 只要有一个视角轨迹是重叠的，则 overlap2D 2D重叠标志位置为True
                        if "cam1" in trackId:
                            overlap2D = (e2Track.cam2frame[0]-e1Track.cam2frame[-1]) <= 0 
                        if "cam2" in trackId:
                            overlap2D = (e2Track.cam1frame[0]-e1Track.cam1frame[-1]) <= 0

                        if verbose:
                            print("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(e1, e2, e1Track.frame[0], e1Track.frame[-1], e2Track.frame[0], e2Track.frame[-1], overlap3D, overlap2D, frameDiff, posDiff))
                        
                        ## If the tracklets start and ends frames differ too much, ignore it
                        if overlap3D or overlap2D or self.graph.has_edge(e1, e2) or self.graph.has_edge(e2, e1): # Check that the tracklets does not temporally overlap, and that there is not already an edge in the DAG between the two tracklets
                            continue    # 若 3D重叠/2D重叠/两个轨迹结点已经存在边

                        frameDiff = abs(frameDiff)

                        ## calculate Euclidean distance between the tracklet end/start points    计算轨迹起始点到终点的欧氏距离        
                        if frameDiff != 0:    # 时间距离不等于0
                            speed = posDiff/(frameDiff/self.FPS)    # 速度 = 空间距离/(时间距离(帧数)/FPS)
                        else:
                            speed = 0.0

                        ## Calculate a weight value based on the inverse exp CDF that penalises a large distance    计算结点之间的权值
                        moveProb = (1.0-scipy.stats.expon.cdf(speed, scale=self.movErrMean+self.movErrStd)) * np.exp(-frameDiff/self.temporalPenalty)    # 速度 时间距离 惩罚

                        dist = self.graph.nodes[e1]['weight'] + self.graph.nodes[e2]['weight']
                        dist *= moveProb    # 距离等于 （e1的权值+e2的权值）* moveProb

                        if verbose:
                            print("\nEdge: {0} to {1} with weight: {2}".format(e1,e2, dist))
                        self.graph.add_edge(e1,e2,weight=dist)    # 加边
 
            
def combine2DTracklets(df, tm):
    
    ids = df.id.unique() # array containing all unique tracklets ids    # 包含着所有轨迹ID
    drop_idx = [] # list to keep track of which indecies are not kept     
    
    # Iterate over each unique ID in the dataframe
    for iID in ids:
        df_id = df[df.id == iID]  # Sub dataframe, containing all rows relevant for the current ID. Indecies are still that of the main dataframe    取得该ID的行集
        
        frame_count = df_id["frame"].value_counts()  # How many times does a frame occur in the dataframe    # 计算该轨迹各帧号出现的次数
        dual_assignment =  frame_count[frame_count == 2].sort_index() # isolating the frames with multiple assignments    # 得出 出现两次的帧号并

        # GO through each frame with two assignments to the same ID
        for idx, sIdx in enumerate(dual_assignment.items()):
            frame, count = sIdx

            frame_idx = list(df_id[df_id["frame"] == frame].index.values)

            rows = df.iloc[frame_idx]   

            # Check if each of the rows have a detection in a different 2D view, and if so calculate the 3D position 
            if (rows.ix[frame_idx[0]]["cam1_x"] > -1.0 and rows.ix[frame_idx[1]]["cam2_x"] > -1.0) or (rows.ix[frame_idx[0]]["cam2_x"] > -1.0 and rows.ix[frame_idx[1]]["cam1_x"] > -1.0):
                row_max = rows.max()
                drop_idx.extend(frame_idx)

                minErr = np.inf
                minP = None
                minP1 = None
                minP2 = None
                minPt = None

                cam2_list = ["l","c","r"]
                if tm.camera2_useHead:
                    cam2_list = ["kpt"]

                for pt in cam2_list:
                    tr = Triangulate()
                
                    t1Pt = np.asarray([row_max["cam1_x"], row_max["cam1_y"]])
                    t2Pt = np.asarray([row_max["cam2_x"], row_max["cam2_y"]])
                    
                    # 1) Triangulate 3D point
                    p,d = tr.triangulatePoint(t1Pt,
                                            t2Pt,
                                            tm.cams[1],
                                            tm.cams[2],
                                            correctRefraction=True)
                
                    p1 = tm.cams[1].forwardprojectPoint(*p)
                    p2 = tm.cams[2].forwardprojectPoint(*p)
            
                    # 2) Calc re-projection errors
                    pos1 = np.array(t1Pt)
                    err1 = np.linalg.norm(pos1-p1)
                    pos2 = np.array(t2Pt)
                    err2 = np.linalg.norm(pos2-p2)
                    err = err1 + err2     
                    
                    if err < minErr:
                        minErr = err
                        minP = p
                        minP1 = p1
                        minP2 = p2    
                        minPt = pt
                
                # If the calculated point is within the aquairum, add it to the df, else do nothing

                if tm.withinAquarium(*minP):
                    row_max["3d_x"] = minP[0]
                    row_max["3d_y"] = minP[1]
                    row_max["3d_z"] = minP[2]
                    row_max["err"] = 1-scipy.stats.expon.cdf(minErr, scale=tm.reprojMeanErr)
                    row_max["cam1_proj_x"] = minP1[0]
                    row_max["cam1_proj_y"] = minP1[1]
                    row_max["cam2_proj_x"] = minP2[0]
                    row_max["cam2_proj_y"] = minP2[1]

                    df = df.append(row_max,ignore_index=True)

    
    return df, drop_idx



## ---- Test stuff --- ##
if __name__ == '__main__':

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--path", help="Path to folder")
    
    args = vars(ap.parse_args())
    
    # ARGUMENTS *************
    if args.get("path", None) is None:
        print('No path was provided. Try again!')
        sys.exit()
    else:
        dataPath = args["path"]

    tm = TrackletMatcher(dataPath)    # 创建实例
    tm.createNodes()    # 创建3D结点
    tm.connectNodes3D()    # 连接3D结点

    csv = pd.DataFrame()
    mergedCount = 0    # 重新编号 3D 轨迹ID

    ## While there are still nodes in the graph    当图中仍存在结点
    while(True):
        if(len(tm.graph.nodes) == 0):    # 结点被清空，则退出
            break
        
        ## Find the largest path through the graph
        path = nx.dag_longest_path(tm.graph)    # 返回最长路径
        length = nx.dag_longest_path_length(tm.graph)    # 返回最长路径长度

        allFrames = []
        for p in path:    # 遍历最长路径上的结点 p为nodeName
            allFrames += list(tm.triangulated[p].frame)    # 得到最长路径上的帧号

        toBeRemoved = []
        print("Best path:")
        for p in path:
            print(" ",p)

            # Save triangulated 3D information to CSV
            track3d = tm.triangulated[p]
            
            df = pd.DataFrame({
                'frame':track3d.frame,
                'id':[mergedCount]*len(track3d.frame),
                'err':track3d.errors,
                '3d_x':[q[0] for q in track3d.positions3d],    # 轨迹上3D点的坐标
                '3d_y':[q[1] for q in track3d.positions3d],
                '3d_z':[q[2] for q in track3d.positions3d],
                'cam1_x':[q[0] for q in track3d.cam1positions],    # 轨迹上3D点的坐标在视角1的2D坐标
                'cam1_y':[q[1] for q in track3d.cam1positions],
                'cam2_x':[q[0] for q in track3d.cam2positions],    # 轨迹上3D点的坐标在视角2的2D坐标
                'cam2_y':[q[1] for q in track3d.cam2positions],
                'cam1_proj_x':[q[0] for q in track3d.cam1reprojections],    # 根据3D点重投影到视角1的2D坐标
                'cam1_proj_y':[q[1] for q in track3d.cam1reprojections],
                'cam2_proj_x':[q[0] for q in track3d.cam2reprojections],    # 根据3D点重投影到视角2的2D坐标
                'cam2_proj_y':[q[1] for q in track3d.cam2reprojections],
                'cam1_tl_x': [q[0] for q in track3d.cam1bbox],    # 视角1 旋转矩形的左上角坐标点
                'cam1_tl_y': [q[1] for q in track3d.cam1bbox],
                'cam1_c_x': [q[2] for q in track3d.cam1bbox],    # 视角1 源矩形的中心坐标点
                'cam1_c_y': [q[3] for q in track3d.cam1bbox],
                'cam1_w': [q[4] for q in track3d.cam1bbox],    # 视角1 旋转矩形的宽
                'cam1_h': [q[5] for q in track3d.cam1bbox],    # 视角1 旋转矩形的高
                'cam1_theta': [q[6] for q in track3d.cam1bbox],    # 视角1 旋转矩形的旋转角度
                'cam1_aa_tl_x': [q[7] for q in track3d.cam1bbox],    # 视角1 Bbox矩形左上角的坐标
                'cam1_aa_tl_y': [q[8] for q in track3d.cam1bbox],
                'cam1_aa_w': [q[9] for q in track3d.cam1bbox],    # 视角1 Bbox矩形的宽
                'cam1_aa_h': [q[10] for q in track3d.cam1bbox],    # 视角1 Bbox矩形的高
                'cam1_frame': track3d.cam1frame,    # 视角1的帧号
                'cam2_tl_x': [q[0] for q in track3d.cam2bbox],    # 视角2 旋转矩形的左上角坐标点
                'cam2_tl_y': [q[1] for q in track3d.cam2bbox],
                'cam2_c_x': [q[2] for q in track3d.cam2bbox],    # 视角2 源矩形的中心坐标点
                'cam2_c_y': [q[3] for q in track3d.cam2bbox],
                'cam2_w': [q[4] for q in track3d.cam2bbox],    # 视角2 旋转矩形的宽
                'cam2_h': [q[5] for q in track3d.cam2bbox],    # 视角2 旋转矩形的高
                'cam2_theta': [q[6] for q in track3d.cam2bbox],    # 视角2 旋转矩形的旋转角度
                'cam2_aa_tl_x': [q[7] for q in track3d.cam2bbox],    # 视角2 Bbox矩形左上角的坐标
                'cam2_aa_tl_y': [q[8] for q in track3d.cam2bbox],
                'cam2_aa_w': [q[9] for q in track3d.cam2bbox],    # 视角2 Bbox矩形的宽
                'cam2_aa_h': [q[10] for q in track3d.cam2bbox],    # 视角2 Bbox矩形的高
                'cam2_frame': track3d.cam2frame})    # 视角2的帧号
    
            # Save information from parent tracks which are
            # not already present in the saved 3D track
            for parent in [track3d.cam1Parent, track3d.cam2Parent]:   
                for f in parent.frame:
                    if(f in allFrames):    # 若遇到重叠的帧号，则跳过
                        continue
                    
                    newRow = pd.DataFrame({
                        'frame':[f],
                        'id':[mergedCount],
                        'err':[-1],
                        '3d_x':[-1],
                        '3d_y':[-1],
                        '3d_z':[-1],
                        'cam1_x':[-1],
                        'cam1_y':[-1],
                        'cam2_x':[-1],
                        'cam2_y':[-1],
                        'cam1_proj_x':[-1.0],
                        'cam1_proj_y':[-1.0],
                        'cam2_proj_x':[-1.0],
                        'cam2_proj_y':[-1.0],
                        'cam1_tl_x': [-1.0],
                        'cam1_tl_y': [-1.0],
                        'cam1_c_x': [-1.0],
                        'cam1_c_y': [-1.0],
                        'cam1_w': [-1.0],
                        'cam1_h': [-1.0],
                        'cam1_theta': [-1.0],
                        'cam1_aa_tl_x': [-1.0],
                        'cam1_aa_tl_y': [-1.0],
                        'cam1_aa_w': [-1.0],
                        'cam1_aa_h': [-1.0],
                        'cam1_frame': [-1],
                        'cam2_tl_x': [-1.0],
                        'cam2_tl_y': [-1.0],
                        'cam2_c_x': [-1.0],
                        'cam2_c_y': [-1.0],
                        'cam2_w': [-1.0],
                        'cam2_h': [-1.0],
                        'cam2_theta': [-1.0],
                        'cam2_aa_tl_x': [-1.0],
                        'cam2_aa_tl_y': [-1.0],
                        'cam2_aa_w': [-1.0],
                        'cam2_aa_h': [-1.0],
                        'cam2_frame': [-1]})

                    # Update cam2 with correct 2D positions    取侧视图交集的前后十个点来用修正2D坐标
                    pointType = "kpt"
                    if parent.cam == 2 and not tm.camera2_useHead:    # 若是侧视且不是 FASTER R-CNN-H == 传统
                        maxTemporalDiff = 10    # 最大时间距离
                        indToPoint = {0:"l", 1:"c", 2:"r"}
                        track3DFrames = np.asarray(track3d.frame)    # 交集的帧号集
                        cam2Positions = np.asarray(track3d.cam2positions)    # 交集的侧视2D坐标

                        frameDiff = track3DFrames - f
                        validFrames = track3DFrames[np.abs(frameDiff) <= maxTemporalDiff]    # 交集中 时间距离（帧数）在10及10以内，称为有效帧号
                        

                        hist = np.zeros((3))
                        for f_t in validFrames:
                            ftPoint = np.asarray(cam2Positions[track3DFrames == f_t])    # 求有效帧号的侧视2D坐标
                            points = np.zeros((3))
                            points[0] = np.linalg.norm(np.asarray(parent.getImagePos(f, "l")) - ftPoint)    # 该点至左边缘点的欧氏距离
                            points[1] = np.linalg.norm(np.asarray(parent.getImagePos(f, "c")) - ftPoint)    # 该点至形心的欧氏距离
                            points[2] = np.linalg.norm(np.asarray(parent.getImagePos(f, "r")) - ftPoint)    # 该点至右边缘点的欧氏距离
                            hist[np.argmin(points)] += 1    # 求最小距离，在hist上+1，来统计到底用哪个点来修正
                        
                        if hist.sum() > 0:
                            pointType = indToPoint[np.argmax(hist)]   # 得到修正的类型

                    newRow['cam{0}_x'.format(parent.cam)] = parent.getImagePos(f, pointType)[0]    # 以下用parent track 来更新为重叠部分的数据
                    newRow['cam{0}_y'.format(parent.cam)] = parent.getImagePos(f, pointType)[1]
                    
                    newRow['cam{0}_tl_x'.format(parent.cam)] = parent.getBoundingBox(f)[0]
                    newRow['cam{0}_tl_y'.format(parent.cam)] = parent.getBoundingBox(f)[1]
                    newRow['cam{0}_c_x'.format(parent.cam)] = parent.getBoundingBox(f)[2]                    
                    newRow['cam{0}_c_y'.format(parent.cam)] = parent.getBoundingBox(f)[3]
                    newRow['cam{0}_w'.format(parent.cam)] = parent.getBoundingBox(f)[4]
                    newRow['cam{0}_h'.format(parent.cam)] = parent.getBoundingBox(f)[5]
                    newRow['cam{0}_theta'.format(parent.cam)] = parent.getBoundingBox(f)[6]
                    newRow['cam{0}_aa_tl_x'.format(parent.cam)] = parent.getBoundingBox(f)[7]
                    newRow['cam{0}_aa_tl_y'.format(parent.cam)] = parent.getBoundingBox(f)[8]
                    newRow['cam{0}_aa_w'.format(parent.cam)] = parent.getBoundingBox(f)[9]
                    newRow['cam{0}_aa_h'.format(parent.cam)] = parent.getBoundingBox(f)[10]
                    newRow['cam{0}_frame'.format(parent.cam)] = parent.getVideoFrame(f)
                    
                    df = df.append(newRow)
            csv = csv.append(df)
                       
            # Remove used tracklets
            toBeRemoved.append(p)    # 添加已处理的结点（nodeName） 和 各视角同轨迹ID的结点         
            cam1 = tm.camIdMap[tm.graph.nodes[p]["cam1"]]    
            cam2 = tm.camIdMap[tm.graph.nodes[p]["cam2"]]    
            for e in (cam1+cam2):    # ==== 
                if(e not in toBeRemoved):    # ====
                    toBeRemoved.append(e)    # ====
        for e in toBeRemoved:
           if(tm.graph.has_node(e)):
               tm.graph.remove_node(e)    # 移除已处理的点
        mergedCount += 1    # 处理下一条3D轨迹
        
    csv = csv.sort_values(by=['id', 'frame'], ascending=[True,True])

    # Drop cases with exact same frame, id, and x/y coordinates, for each camera view
    csv = csv.drop_duplicates(['frame','id','cam1_x','cam1_y'])
    csv = csv.drop_duplicates(['frame','id','cam2_x','cam2_y'])
    
    csv.reset_index(inplace=True, drop=True)
    csv, drop_idx = combine2DTracklets(csv, tm)
    csv = csv.drop(drop_idx)
    csv = csv.sort_values(by=['id', 'frame'], ascending=[True,True])    # 根据ID frame 升序
    
    csv.reset_index(inplace=True, drop=True)

    # Find cases where there are several rows for the same frame in a single Tracklet, and determines which ones minimize the 3D distance (and therefore should be kept)
    csv = csv.drop(getDropIndecies(csv, True))

    outputPath = os.path.join(dataPath, 'processed', 'tracklets_3d.csv')    # 保存
    print("Saving data to: {0}".format(outputPath))
    csv.to_csv(outputPath)