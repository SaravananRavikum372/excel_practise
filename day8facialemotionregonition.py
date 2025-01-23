# Import facial emotion recognition core lib
from facial_emotion_recognition import EmotionRecognition 
import cv2

# Create an EmotionRecognition object with device='cpu'
er=EmotionRecognition(device='cpu')

# Open a video capture stream
cam = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    _, img = cam.read()

    # Recognize emotion and get the processed image
    img = er.recognise_emotion(img, return_type='BGR')

    # Display the processed image
    cv2.imshow('Emotion Recognition', img)

    # Break the loop if the 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
