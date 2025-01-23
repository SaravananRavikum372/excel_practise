# next can see the rectangle for usage anyone of them object moving it will draw one rectangle and put the text
#cv2.rectangle(srcimg,startingpoint,endingpoint,color,thickness)
#cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#w-widthend,h-heightend x,y-startpointofrectangle
#and color 0-nocolor like 255or 100 any value defend means color like color will enable RGB (RED,GREEN,BLUE)

#next see the put text in image
#cv2.putText(srcimg,text,position,font,fontSize,color,thickness)
#cv2.putText(img,text,(10,16),cv2.FONT_HERSHEY_SIMPLEX,10,(0,255,0),2)

#findcontour the image

#cv2.findContours(srcimgcopy,contourRetrievalmode,contourApproximateMethod)

#cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL,CV2.CHAIN_APPROX_SIMPLE)

