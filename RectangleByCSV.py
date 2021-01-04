import numpy as np
import cv2
import glob
import os
import string
import pandas as pd

# WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\imgF' #存放正视图图片的文件夹路径  
WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\imgF' #存放顶视图图片的文件夹路径

paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.jpg'))
paths.sort()

# savepath = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\Detect_F\\' #存放保存好修正图片的文件夹路径 
savepath = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\Detect_F\\' #存放保存好修正图片的文件夹路径 

# csvpath = 'D:\\Github\\ZebraFish-MOT\\DetectCSV\\boundingboxes_2d_04_T_cam1.csv'
csvpath = 'D:\\Github\\ZebraFish-MOT\\DetectCSV\\boundingboxes_2d_03_F_cam2.csv'
Dataframe = pd.read_csv(csvpath)
# print(Dataframe.UpperLeftCornerX[2])

CountImage = 1
CountText = 0
color = color = (0,0,255)
font = cv2.FONT_HERSHEY_SIMPLEX
for path in paths:
    img = cv2.imread(path)

    while((CountText<Dataframe.shape[0])&(Dataframe.Frame[CountText]==CountImage)):
        
        if((Dataframe.Confidence[CountText]>0.90)&(Dataframe.UpperLeftCornerX[CountText]<2400.0)&(Dataframe.LowerRightCornerY[CountText]<1470.0)):  
        
            TopLeft = (int(Dataframe.UpperLeftCornerX[CountText]),int(Dataframe.UpperLeftCornerY[CountText]))
            DownRight = (int(Dataframe.LowerRightCornerX[CountText]),int(Dataframe.LowerRightCornerY[CountText]))

            cv2.putText(img,str(round(Dataframe.Confidence[CountText]*100,2)),TopLeft, font, 1,(255,0,0),2,cv2.LINE_AA)
            # print(str(round(Dataframe.Confidence[CountText]*100,2)))
            cv2.rectangle(img,TopLeft , DownRight, color, 2)
        CountText = CountText + 1
        print(str(CountText)+"/"+str(Dataframe.shape[0]))
        if(CountText==Dataframe.shape[0]):
            break


    Filename = savepath + str(CountImage).rjust(6,'0')+ '.png'
    # print(Filename)

    cv2.imwrite(Filename, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    # print(CountImage)

    CountImage = CountImage + 1
    # cv2.imshow("Image",img)

    if(cv2.waitKey(1) == 27):
        break

print("Done")