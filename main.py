import cv2
import os

# Constants
MODEL_PATH = os.path.join("dnn_model", "yolov4-tiny.weights")
CFG_PATH = os.path.join("dnn_model", "yolov4-tiny.cfg")
CLASSES_PATH = os.path.join("dnn_model", "classes.txt")

# Open cv DNN
net = cv2.dnn.readNet(MODEL_PATH, CFG_PATH)
model = cv2.dnn_DetectionModel(net)
#model.setInputParams(size=(416, 416), scale=1/255)  # size must be divided by 8

# Example 1: Larger Input Size
model.setInputParams(size=(608, 608), scale=1/255)




# Example 2: Smaller Input Size
model.setInputParams(size=(320, 320), scale=1/255)

# Example 3: Different Scale
model.setInputParams(size=(416, 416), scale=1/127)  # Adjust the scale value

#model.setInputParams(size=(960, 960), scale=1/255)
# Load class Lists
classes = []
with open(CLASSES_PATH, "r") as file_object:
    classes = [class_name.strip() for class_name in file_object.readlines()]

# Initialize the camera
camera_index = 0
cap = cv2.VideoCapture(camera_index)
cap = cv2.VideoCapture("los_angeles.mp4")
#cap = cv2.VideoCapture("The Movement Of Vehicles On Road India Stock Footage SBV-322513033 - Storyblocks - Brave 2023-07-03 10-44-10.mp4")

new_width = 1920
new_height = 1080

while True:
    # Get frames
    ret, frame = cap.read()
    if not ret:
        break

    # Resizing the frame
    frame = cv2.resize(frame, (new_width, new_height))

    # Object Detection
    class_ids, scores, bboxes = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        x, y, w, h = bbox

        cv2.putText(frame, classes[class_id], (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 244, 203), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (235, 211, 201), 2)
        score_text = f"Score: {score:.2f}"
        cv2.putText(frame, score_text, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    cv2.imshow('Object Detection and Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
