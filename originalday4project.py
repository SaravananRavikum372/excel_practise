import cv2
import imutils
# import time  # Uncomment if needed for delay

cap = cv2.VideoCapture(0)  # cam id
# time.sleep(1)

firstFrame = None # None it means specify the null value or empty
area = 500

while True:
    _, img = cap.read()  # why using dash means because the read function returns two values: true or false and img
    text = "normal"
    # so I would not like to store the true or false value so will using the dash instead using any variable

    cv2.imshow('live capture', img)  # it will display the live capture img

    # in looping true is infinite condition it means function read continuously camid

    # next calculating, so convert img into grayscale and before resize the img

    img = cv2.resize(img, (700, 800))  # resize using cv2
    # next change the grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (21, 21), 0)  # smoothed img

    if firstFrame is None:      # is keyword like AND, OR,NOT, IS an keyword it will is true or false means here or not
        firstFrame = blur_img  # capturing the first frame
        continue
    img_diff = cv2.absdiff(firstFrame, blur_img)  # absolute difference
    thresh_img = cv2.threshold(img_diff, 30, 255, cv2.THRESH_BINARY)[1]  # finally find the threshold black=0and 30 to255 is white
    # cv2.imshow('thresh_img', thresh_img)  # -before using dilate
    thresh_img = cv2.dilate(thresh_img, None, iterations=2)  # left over the erosion or says some small bit of white shade
    thresh_dup = thresh_img.copy()
    contours = cv2.findContours(thresh_dup, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # it will find no of object
    # border -- contour
    contours = imutils.grab_contours(contours)
    for c in contours:
        if cv2.contourArea(c) < area:  # if the contour border area is large compared to defined area, continue executing
            continue  # otherwise false means other statement will be executed
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving object detected"
        print(text)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('camera_feed', img)
        key = cv2.waitKey(10)
        print(key)
        if key == ord("a"):
            break

cap.release()
cv2.destroyAllWindows()
