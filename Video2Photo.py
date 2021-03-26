import cv2 
savepath = "E:\\FFOutput\\Sync\\ZebraFish-01\\imgT\\"

videopath = "E:\\FFOutput\\Sync\\cam1_1.mp4"
cap = cv2.VideoCapture(videopath) 
CountImage = 1
while(cap.isOpened()): 
    ret, frame = cap.read() 
    Filename = savepath + str(CountImage).rjust(6,'0')+ '.jpg'
    CountImage +=1
    cv2.imwrite(Filename, frame,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    print(Filename)
cap.release() 
cv2.destroyAllWindows()