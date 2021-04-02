import numpy as np
import pandas as pd
import glob
import os
import string

path ='D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\gt\\'
GroundTruth = np.loadtxt(path+'gt.txt', delimiter=',' , usecols=[0,1,2,3,4])

df_gt = pd.DataFrame(GroundTruth)
df_gt.to_csv(path+'gt.csv',header=0,index=0)
print("Done")