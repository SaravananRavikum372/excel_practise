import cv2
img=cv2.imread('logo.png')# imread is used for read the image 
cv2.imshow('logo',img)# imshow is used for show the image like display the image
cv2.imwrite('logo1.jpg',img) #imwrite is used for save image for like change format
#cv2.waitKey(3000)
#cv2.destroyAllWindows()
img1=cv2.imread('logo1.jpg')
#cv2.imshow('format',img2)
greyimg=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayimg',greyimg)
cv2.imwrite('grayimg.jpg',greyimg)
print(img.shape)
print(img.size)
