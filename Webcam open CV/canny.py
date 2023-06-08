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

# Apply the Canny edge filter to the frame
edges = cv2.Canny(frame, 100, 200)  # You can adjust the threshold values (100 and 200) as per your preference

# Display the captured frame and the edges
cv2.imshow("Webcam Frame", frame)
cv2.imshow("Canny Edges", edges)

# Wait for a key press
cv2.waitKey(1)

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
