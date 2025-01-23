# reading frame from the camera
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("The capture is true; it is opened")
    cap.set(cv2.CAP_PROP_MODE, 1)

    # Read a frame
    ret, frame = cap.read()

    # Check if the frame is valid
    if ret:
        # Resize the frame
        frame = cv2.resize(frame, (700, 800))

        # Display the frame
        cv2.imshow('Live Capture', frame)
    else:
        print("Error: Couldn't read a frame")
else:
    print("The capture is false; it is not opened")

# Release the video capture object and close the window
#cap.release()
#cv2.destroyAllWindows()
