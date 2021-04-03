import numpy as np
import glob
import os
import string
import pandas as pd
from lxml.etree import Element, SubElement, tostring

#GroundTruth = np.loadtxt('D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\gt\\gt.txt', delimiter=',' , usecols=[0,5,6,11]) #存放顶视图GroundTruth的文件夹路径 TOP
GroundTruth = np.loadtxt('D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-02\\gt\\gt.txt', delimiter=',' , usecols=[0,12,13,18])      #存放正视图GroundTruth的文件夹路径 Front
print(GroundTruth.shape)

#radius = [25,25]    #======================
radius = [12,13]

def Single_txt2xml(count,xml_path):
    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'Zebrafish-02-F'                    #=============================
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = str(count).rjust(6,'0')+".jpg"
    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = "2704"
    node_height = SubElement(node_size, 'height')
    node_height.text = "1520"
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    rows = GroundTruth[GroundTruth[:,0]==count]
    for row in rows:
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = "Zebrafish"
        node_pose=SubElement(node_object, 'pose')
        node_pose.text="Unspecified"
        node_truncated=SubElement(node_object, 'truncated')
        node_truncated.text= str(int(row[3]))
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(round(row[1] - radius[0]))

        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(round(row[2] - radius[0]))

        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(round(row[1] + radius[1]))

        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(round(row[2] + radius[1]))

    xml = tostring(node_root, pretty_print=True)                    # 格式化显示，该换行的换行
    img_newxml = os.path.join(xml_path)
    file_object = open(img_newxml, 'wb')
    file_object.write(xml)
    file_object.close()
    print(count)

count = 1
while(count<=900):            #=====================01-7188 02-900
    Filename = "D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-02\\XML-F-Head\\" + str(count).rjust(6,'0')+ '.xml'  #=====================
    Single_txt2xml(count,Filename)
    count = count + 1
print("Done")