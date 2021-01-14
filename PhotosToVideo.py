import numpy as np
import cv2
import glob
import os

# WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\gt_F\\'   #存放保存好修正图片的文件夹路径 
# WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\Detect_F\\'    #存放保存好修正图片的文件夹路径 
# WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-04\\imgT\\'    #存放保存好修正图片的文件夹路径 
WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\MatplotlibTracklet\\F\\'
paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.png'))
# paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.jpg'))
paths.sort()

fourcc =cv2.VideoWriter_fourcc('M','J','P','G')   # 保存视频的编码
# out = cv2.VideoWriter("ZebraFish-04-F-Tracklet.avi", fourcc, 60.0, (2704, 1520))
out = cv2.VideoWriter("ZebraFish-01-F-Tracklet.avi", fourcc, 60.0, (700, 700))
# out = cv2.VideoWriter("ZebraFish-02-X-Tracklet.avi", fourcc, 60.0, (721, 724))
for path in paths:
    videoPlay = cv2.imread(path)
    out.write(videoPlay)
    print(path)

out.release()
print("Done")