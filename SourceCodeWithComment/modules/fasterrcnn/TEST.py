import sys
import base64
import time

def ImageDecode(strs):
    imgdata=base64.b64decode(strs)
    file=open('LRL.jpg','wb')
    print("Save Successfully")
    file.write(imgdata)
    file.close() 

def ImageEncode():
    file= open('ljj.jpg', 'rb')
    img = base64.b64encode(file.read())
    print("Encode Successfully")
    file.close() 
    return img    

ImageDecode(ImageEncode())