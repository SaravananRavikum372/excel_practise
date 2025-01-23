import cv2

while True:
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
       # print("The capture is true; it will capture img")
        # cap.set(cv2.CAP_PROP_MODE, 1)

        ret, frame = cap.read()

        if ret:
            frame = cv2.resize(frame, (800, 600), 50)
            pre_frame = frame.copy()

            # cv2.imshow('livecapture', frame)
            grayimg = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('grayimg', grayimg)
            threshimg = cv2.threshold(grayimg, 30, 255, cv2.THRESH_BINARY)[1]
           # cv2.imshow('threshimg', threshimg)

            contour, _ = cv2.findContours(threshimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contours in contour:
                x, y, w, h = cv2.boundingRect(contours)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 15)
                cv2.putText(frame, 'movingobject', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 4)
                cv2.imshow('movingobjectdetction', frame)
                pre_frame = frame.copy()
        else:
            print("Error: The image could not be captured")
    else:
        print("The capture is false; it will not capture img")

    # Release the video capture object and close all windows
    cap.release()

    # Break the loop when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
