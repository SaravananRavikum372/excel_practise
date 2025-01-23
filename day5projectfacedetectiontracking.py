# project of advanced face detection and tracking
#using computer vision of opencv -- cv2 and haar cascade frontelface algorithm
import cv2
alg="haarcascade_frontalface_default.xml"
haarCascade=cv2.CascadeClassifier(alg)
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haarCascade.detectMultiScale(grayimg,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4) # -- let see (0,255,0) is blue ,green, red and 0 means disable the color
    cv2.imshow('facedetection',img)
    key=cv2.waitKey(1)
    print(key)
    if key==ord("a"):
         break
cap.release()
cv2.destroyAllWindows()
