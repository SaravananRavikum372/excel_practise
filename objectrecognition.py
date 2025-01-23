import numpy as np
import imutils as im
import time
import cv2

prototxt="MobileNetSSD_deploy.prototxt"
model="MobileNetSSD_deploy.caffemodel"
confThresh=0.2  #confidialthreshhold value

CLASSES=["background","aeroplane","bicycle","bird","boat","bottle","bus","car","cat","chair","cow","diningtable","dog",
                       "horse","motorbike","person","pottedplant","sheep","sofa","train","tvmonitor","mobile"]  #classes is an output
color = np.random.uniform(0, 255, size=(len(CLASSES), 3)) #like 3 is RGB COLOR AND 1 means binary gray color

print("loading model")

net=cv2.dnn.readNetFromCaffe(prototxt,model)#loading predrained model syntax of cv2.dnn.readNetFrameCaffe

print("model loaded")
print("starting camera feeding")

cap=cv2.VideoCapture(0)
time.sleep(3)  # delay function

while True:
         _,frame=cap.read()
         frame= imutils.resize(frame, width=1000)
         (h,w)=frame.shape[:,2] #frame.shape is used for finding height width and channel means color or binary now will get only height and width so use [:,2]
         imResizeBlob=cv2.resize(frame,(300,300))
         Blob=cv2.dnn.blobFromImage(imResizeBlob,0.007843,(300,300),127.5)# image preprocessing for means binary large object
         net.setInput(Blob)
         detection=net.forward()
         print(detection)
         detshape=detection.shape[2]
         print(detshape)





