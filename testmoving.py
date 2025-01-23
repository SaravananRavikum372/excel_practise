import cv2

cap = cv2.VideoCapture(0)

if (cap.isOpened()):
    print("The capture is true; it will capture img")
    ret, frame = cap.read()

    if ret:
        print("The capture frame is valid")
        frame = cv2.resize(frame, (800, 600), 50)
        pre_frame = frame.copy()

        # Convert the frame to grayscale
        grayimg = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)

        # Apply threshold to the grayscale image
        _, threshimg = cv2.threshold(grayimg, 30, 255, cv2.THRESH_BINARY)

        # Find contours in the binary image
        contours, _ = cv2.findContours(threshimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 15)
            cv2.putText(frame, 'Moving Object', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 4)

        cv2.imshow('Moving Object Detection', frame)
        pre_frame = frame.copy()  # Fix: Added parentheses to call the 'copy' method

    else:
        print("Error: The image could not be captured")

else:
    print("The capture is false; it will not capture img")

cv2.waitKey(0)
cv2.destroyAllWindows()
