import numpy as np
import glob
import os
import string
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--path", help="Path to csv")
ap.add_argument("-c", "--camId", help="Camera ID. top = 1 front = 2 hade = 3")
# ap.add_argument("-v", "--video", action='store_true', help="Save video")
# ap.add_argument("-i", "--images", action='store_true', help="Display images")
args = vars(ap.parse_args())
csvpath = args["path"]
camId = int(args["camId"])
# savepath = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\MatplotlibTracklet\\Test\\' #存放保存好修正图片的文件夹路径 

Dataframe = pd.read_csv(csvpath)
# Dataframe1=Dataframe.sort_values('frame',inplace=True,ascending=True)
i=1
MaxNumber = Dataframe['frame'].max()

fig = plt.figure(figsize=(8,7))

while(i<=MaxNumber):
    Data=Dataframe.loc[Dataframe['frame'] == i]
    ax = Axes3D(fig)
    if(Data.empty==False):   
        # print(Data.shape[0]) 
        # print(Data)
        for row in range(Data.shape[0]): 
            ax.set_xlim(0,30)
            ax.set_ylim(0,30)
            ax.set_zlim(0,30)
            if(camId==1):
                ax.view_init(elev=-90, azim=270)      #顶视图
            elif(camId==2):
                ax.view_init(elev=-180, azim=270)     #正视图
            elif(camId==3):
                ax.view_init(elev=-180+30, azim=270-50) #斜视图

            RowData = Data.iloc[row]
            if(RowData['id'] == 0):
                color = 'red' 
                mark = 'o'
            if(RowData['id'] == 1):
                color = 'green' 
                mark = 'o'
            if(RowData['id'] == 2):
                color = 'blue'
                mark = 'o'
            if(RowData['id'] == 3):
                color = 'yellow'
                mark = 'o'
            if(RowData['id'] == 4):
                color = 'magenta'
                mark = 'o'
            if(RowData['id'] == 5):
                color = 'cyan'
                mark = 'o'
            if(RowData['id'] == 6):
                color = 'black'
                mark = 'o'            

            if(RowData['id'] == 7):
                color = 'red' 
                mark = 'x'
            if(RowData['id'] == 8):
                color = 'green' 
                mark = 'x'
            if(RowData['id'] == 9):
                color = 'blue'
                mark = 'x'
            if(RowData['id'] == 10):
                color = 'yellow'
                mark = 'x'
            if(RowData['id'] == 11):
                color = 'magenta'
                mark = 'x'
            if(RowData['id'] == 12):
                color = 'cyan'
                mark = 'x'
            if(RowData['id'] == 13):
                color = 'black'
                mark = 'x'

            x = RowData['3d_x']
            y = RowData['3d_y']
            z = RowData['3d_z']
            
            print(str(RowData['3d_x'])+" "+str(RowData['3d_y'])+" "+str(RowData['3d_z']))

            
            ax.scatter(x,y,z,c=color,marker=mark )
        # Filename = savepath + str(i).rjust(6,'0')+ '.png'
        print("frame = "+str(i))
        #plt.savefig(Filename,bbox_inches = 'tight',pad_inches = 0)     # 保存图片
        plt.pause(0.00000000000000000000000000000000000000001)    # 显示图片
        plt.clf()
    i+=1
print("Done")