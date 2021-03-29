import cv2 
savepath = "E:\\FFOutput\\Sync\\ZebraFish-03\\imgT\\"

videopath = "E:\\FFOutput\\Sync\\cam1_3.mp4"
cap = cv2.VideoCapture(videopath) 
CountImage = 1
FrameNumber = int(cap.get(7))
print(FrameNumber)
while(CountImage<=FrameNumber): 
    ret, frame = cap.read() 
    Filename = savepath + str(CountImage).rjust(6,'0')+ '.jpg'
    # cv2.imshow("dada",frame)
    cv2.imwrite(Filename, frame,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    print(CountImage)
    # cv2.waitKey(1)
    CountImage +=1
cap.release() 
cv2.destroyAllWindows()