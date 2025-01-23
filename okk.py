#cv2.GaussianBlur(img, (21,21),0) -default value is 21,21
#cv2.threshold(grayimg, 150,255,cv2.THRESH_BINARY) [1]- threshold
#cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) -colorimg to grayimg
#cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) - (0,255,0),2) - color and thickness
#cv2.putText(img, text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)- 0.5 is fontsize and next same color thickness
#cv2.findContours(threshimg,cv2.RETR_EXTERNAL,CV2.CHAIN_APPROX_SIMPLE)

     #IMPORT CV2
    #VS=cv2.VideoCapture(0)
   # while True:
     #   img=vs.read()-------------------------- read() - will return two value one is true or false and another one is img
       # cv2.imshow("livevideo",img)
        #key=cv2.waitKey(1)
        #if key==ord("q"):
          #  break
        #vs.release()
        #cv2.destroyAllWindows()
        
