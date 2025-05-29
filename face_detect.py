import torch
import cv2

# Load YOLOv5s pre-trained model from PyTorch Hub (detects 80 classes incl. people & common animals)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Render results on the frame
    annotated_frame = results.render()[0]

    # Show the frame
    cv2.imshow('YOLOv5 Human & Animal Detection', annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
