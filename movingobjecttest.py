import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Couldn't open camera.")
    exit()

# Read the first frame
ret, prev_frame = cap.read()
prev_frame = cv2.resize(prev_frame, (700, 800))

while True:
    # Read the current frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (700, 800))

    if not ret:
        print("Error: Couldn't read frame.")
        break

    # Convert frames to grayscale
    gray_prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the current and previous frames
    diff = cv2.absdiff(gray_frame, gray_prev_frame)

    # Apply a threshold to create a binary image
    _, threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshim',threshold)

    # Find contours in the binary image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the moving objects and add text
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Moving Object', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the current frame with moving object detection
    cv2.imshow('Moving Object Detection', frame)

    # Update the previous frame
    prev_frame = frame.copy()

    # Break the loop when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
