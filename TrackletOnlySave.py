import numpy as np
import glob
import os
import string
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

savepath = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\MatplotlibTracklet\\Test\\' #存放保存好修正图片的文件夹路径 
csvpath = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-03\\processed\\tracks_3d_interpolated.csv'
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
            # ax.view_init(elev=-90, azim=270)      #顶视图
            # ax.view_init(elev=-180, azim=270)     #正视图
            ax.view_init(elev=-180+45, azim=270-45) #斜视图

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
            # print(str(x)+"  "+str(y)+"  "+str(z))
            
            ax.scatter(x,y,z,c=color,marker=mark )
        Filename = savepath + str(i).rjust(6,'0')+ '.png'
        print(Filename)
        #plt.savefig(Filename,bbox_inches = 'tight',pad_inches = 0)     # 保存图片
        plt.pause(0.00000000000000000000000000000000000000001)    # 显示图片
        plt.clf()
    i+=1
print("Done")