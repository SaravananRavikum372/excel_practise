import cv2
import imutils
img=cv2.imread('logo.png')
cv2.imshow('firstimg',img)
resizedimg=imutils.resize(img,width=700)
cv2.imshow('resizedimg',resizedimg)
cv2.imwrite('resize.jpg',resizedimg)
