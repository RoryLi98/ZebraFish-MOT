import numpy as np
import cv2
import glob
import os
import string

GroundTruth = np.loadtxt('D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\gt\\gt.txt', delimiter=',' , usecols=[0,1,14,15,16,17])
print(GroundTruth.shape)
print(GroundTruth.shape[0])
WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\imgF'#存放图片的文件夹路径
paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.jpg'))
paths.sort()

savepath = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\gt_F\\'
CountImage = 1
CountText = 0
color = (255,255,255)
for path in paths:
    img = cv2.imread(path)
    GroundRow = GroundTruth[CountText]
 
    while((GroundRow[0]==CountImage)&(CountText<GroundTruth.shape[0])):
        TopLeft = (int(GroundRow[2]),int(GroundRow[3]))
        DownRight = (int(GroundRow[2])+int(GroundRow[4]),int(GroundRow[3]+int(GroundRow[5])))

        if(GroundRow[1] == 1):
            color = (0,0,255)
        if(GroundRow[1] == 2):
            color = (0,255,0)
        if(GroundRow[1] == 3):
            color = (255,0,0)
        if(GroundRow[1] == 4):
            color = (0,255,255)
        if(GroundRow[1] == 5):
            color = (255,0,255)
        if(GroundRow[1] == 6):
            color = (255,255,0)
        if(GroundRow[1] == 7):
            color = (79,79,47)
        if(GroundRow[1] == 8):
            color = (255,144,30)
        if(GroundRow[1] == 9):
            color = (128,0,0)
        if(GroundRow[1] == 10):
            color = (0,128,0)

        cv2.rectangle(img,TopLeft , DownRight, color, 2)
        # print(GroundRow)
        CountText = CountText + 1
        print(CountText)
        if(CountText<GroundTruth.shape[0]):
            GroundRow = GroundTruth[CountText]



    Filename = savepath + str(CountImage).rjust(6,'0')+ '.png'
    # print(Filename)

    cv2.imwrite(Filename, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    # print(CountImage)

    CountImage = CountImage + 1
    # cv2.imshow("Image",img)

    if(cv2.waitKey(1) == 27):
        break
print("Done")

