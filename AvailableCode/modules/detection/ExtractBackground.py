import cv2
import argparse
import os.path
import sys
import configparser
import numpy as np
sys.path.append('../../')
from common.utility import *

class BackgroundExtractor():
    """
    Class implementation for background subtraction
    """
    
    def __init__(self, dataPath, camId, video=False):
        """
        Initialize object
        
        Input:
            vidPath: Path to the video files
        """
        
        print("BackgroundExtractor initialized.")
        
        self.bgPath = os.path.join(dataPath, 'background_cam{0}.png'.format(camId))
        self.video = video

        if self.video:
            self.vidPath = os.path.join(dataPath, 'cam{0}.mp4'.format(camId))

            # Load video
            cap = cv2.VideoCapture(self.vidPath)
        
            # Close program if video file could not be opened
            if not cap.isOpened():
                print("Could not open file: {0}".format(self.vidPath))
                sys.exit()
            self.cap = cap
        else:
            self.imgPath = os.path.join(dataPath, 'cam{0}'.format(camId))
        
            if not os.path.isdir(self.imgPath):
                print("Could not find image folder {0}".format(self.imgPath))
                sys.exit()


        if(os.path.isfile(self.bgPath)):
            print("Background file already exists. Exiting...")
            return
        # self.n_median = 80
        self.loadSettings(dataPath)


    def loadSettings(self,path):
        """
        Load settings from config file in the provided path.
        
        Config file includes information on the following, which is set in the object:
            n_median: Number of images to use for calculating the median image
            
        Input:
            path: String path to the folder where the settings.ini file is located
        """
        
        config = readConfig(path)
        c = config['BackgroundExtractor']
        self.n_median = c.getint("n_median")


    def _collectSamplesVideo(self, verbose = False):
        """
        Sample frames for the background calculation by extracting them from the defined video.

        Input:
            verbose: Whether to print information regarding which frames are used
        """

        cap = self.cap
        # Collect sample images from the video
        imgs = []
        numSamples = self.n_median
        maxFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        sampleFrames = np.linspace(0,maxFrames,numSamples+2)[1:-1]


        for f in sampleFrames:
            if verbose:
                print("Extracting image from frame: {0}".format(int(f)))
            cap.set(cv2.CAP_PROP_POS_FRAMES,int(f))
            ret, frame = cap.read()
            if(ret):
                imgs.append(frame)
        self.imgs = imgs
        
        
    def _collectSamplesImg(self, verbose = False):
        """
        Sample frames for the background calculation by extracting them from the prior extracted image files.

        Input:
            verbose: Whether to print information regarding which frames are used
        """

        imgs = []
        frames = [f for f in sorted(os.listdir(self.imgPath)) if os.path.splitext(f)[-1] in [".png", ".jpg"]]
        numSamples = self.n_median
        maxFrames = len(frames)
        sampleFrames = np.linspace(0, maxFrames, numSamples, endpoint = False, dtype=np.int)

        for f in sampleFrames:
            if verbose:
                print("Extracting image from frame: {0}".format(int(f)))
            frame = cv2.imread(os.path.join(self.imgPath, frames[f]))
            if frame is not None:
                imgs.append(frame)
        self.imgs = imgs




    def collectSamples(self, verbose = False): 
        """
        Collect samples to be used when calculating background image.
        The images are sampled at uniform intervals throughout the provided video or img folder
        """
        
        if self.video:
            self._collectSamplesVideo()
        else:
            self._collectSamplesImg()
    

    def createBackground(self):
        """
        Compute the median image of the collected samples.
        
        Output:
            bg: The computed background image
        """
        
        try:
            # Merge samples into background and save
            print("Generating background from {0} samples".format(len(self.imgs)))
            stack = np.stack(self.imgs)
            bg = np.median(stack, axis=0)
            return bg
        except:
            print("No images given. Run BackgroundExtractor.collectSamples before trying to create a background")
            sys.exit() 


if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--path", help="Path to the directory containing the video file")
    ap.add_argument("-c", "--camera", help="The ID of the camera to process. Top = 1. Front = 2.")
    
    args = vars(ap.parse_args())

    if args.get("path", None) is None:
        print('No path was provided. Try again!')
        sys.exit()
    else:
        path = args["path"]
    
    if args.get("camera", None) is None:
        camId = 1
        print('No camera ID was given. Using default ID of: {0}'.format(camId))
    else:
        camId = int(args["camera"])
     
    # Prepare path
    bgPath = os.path.join(path, 'background_cam{0}.png'.format(camId))

    bgExt = BackgroundExtractor(path, camId)
    bgExt.collectSamples()
    bg = bgExt.createBackground()
    cv2.imwrite(bgPath, bg)