import os
import cv2

# Initializing the algorithm of Haar Cascade frontal face
alg = "haarcascade_frontalface_default.xml"

# Loading the algorithm into the variable
haarcascade = cv2.CascadeClassifier(alg)

# Create a path for saving the image data
dataset = "D:/datacollection/saravanan"
folder_name = "myname"
path = os.path.join(dataset, folder_name)  # Creating a path for the folder

# Next, create a folder for a specific path
if not os.path.exists(path):  # Check if the folder is created or not in the specific path
    os.makedirs(path)  # Use os.makedirs to create the folder and any necessary parent folders
    
cap = cv2.VideoCapture(0)
count = 1

while count <= 51:
    _, img = cap.read()
    print("count", count)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haarcascade.detectMultiScale(gray_img, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        face = gray_img[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (150, 160))
        cv2.imwrite(os.path.join(path, f'face_{count}.png'), face_resize)

    count += 1
    cv2.imshow('face', img)
    key = cv2.waitKey(10)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
