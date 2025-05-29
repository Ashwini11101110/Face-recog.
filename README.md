# Face Detection Project

## Overview
This project implements a face detection system using a pre-trained YOLOv5s model. It can detect faces in images or video streams with high accuracy and speed.

## Features
- Real-time face detection using YOLOv5s.
- Easy to run with Python.
- Uses a lightweight pre-trained model (`yolov5s.pt`).
- Simple and modular Python script (`face_detect.py`).

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   cd REPO_NAME
(Optional but recommended) Create a virtual environment:


python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
Install required packages:


pip install -r requirements.txt
(Note: Create a requirements.txt with needed dependencies like torch, opencv-python, etc.)

Usage
Run the face detection script:


python face_detect.py --source path_to_image_or_video
Replace path_to_image_or_video with your input file or use 0 for webcam.

Files
1: face_detect.py — Main Python script for face detection.

2: yolov5s.pt — Pre-trained YOLOv5s model weights.

3: .gitignore — Specifies files and folders to ignore in Git.
