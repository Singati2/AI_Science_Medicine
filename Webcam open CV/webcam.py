import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Could not open webcam")
    exit()

# Read a frame from the webcam
ret, frame = cap.read()

# Check if the frame was successfully read
if not ret:
    print("Failed to capture frame from webcam")
    exit()

# Display the captured frame
cv2.imshow("Webcam Frame", frame)

# Wait for a key press
cv2.waitKey(1)

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
