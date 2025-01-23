import cv2
img=cv2.imread('logo.png')
cv2.imshow('originalimg',img)
imgblur1=cv2.GaussianBlur(img,(21,21),750)
imgblur2=cv2.GaussianBlur(img,(21,21),12)
#cv2.imshow('blur1',imgblur1)
#cv2.imshow('blur2',imgblur2)
cv2.imwrite('blur1.jpg',imgblur1)
cv2.imwrite('blur2.jpg',imgblur2)
#next see the threshold value
#first color image is convert into grey next fully change black and white
#0-black, 255-white  180-threshold means up and down in between start value
greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #original img is convert into greyimg
#threshhold(sourceimg, thresholdval,maximumval,cv2.thresh_binary) 1is mention as img and 0 means it will take value
thresholdimg1=cv2.threshold(greyimg,150,255,cv2.THRESH_BINARY)[1] #in first thresh hold value is accurate correct
thresholdimg2=cv2.threshold(greyimg,145,255,cv2.THRESH_BINARY)[1]
thresholdimg3=cv2.threshold(greyimg,100,255,cv2.THRESH_BINARY)[1]
thresholdimg4=cv2.threshold(greyimg,150,255,cv2.THRESH_BINARY)[1]
thresholdimg5=cv2.threshold(greyimg,180,255,cv2.THRESH_BINARY)[0]
#cv2.imshow('greyimg',greyimg)
#cv2.imshow('thr1',thresholdimg1)
#cv2.imshow('thr2',thresholdimg2)
#cv2.imshow('thr3',thresholdimg3)
#cv2.imshow('thr4',thresholdimg4)
cv2.imshow('thr5',thresholdimg5)
