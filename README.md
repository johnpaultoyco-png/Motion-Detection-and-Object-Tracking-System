# Motion Detection and Object Tracking System

## CSC 126 Computer Vision Midterm Project

### Description

The Motion Detection and Object Tracking System is a Python desktop application that uses OpenCV to detect movement through a webcam.

The system compares consecutive video frames and identifies areas where significant changes occur. Detected moving regions are displayed using bounding boxes.

### Objectives

- Detect motion using a webcam.
- Apply image processing techniques.
- Segment moving regions from the background.
- Detect contours.
- Display bounding boxes around moving regions.

### Features

- Real-time motion detection using a webcam.
- Moving object detection using frame comparison or background subtraction.
- Bounding boxes around detected moving objects.
- Live video display with motion detection results.
- Video file support, if implemented.
- Simple and beginner-friendly interface.

### Computer Vision Topics Used

1. Image Operations
2. Image Segmentation
3. Motion and Object Tracking

### Technologies

- Python
- OpenCV
- NumPy

### Requirements

- Python 3.x
- Webcam
- Windows/macOS/Linux
- OpenCV
- NumPy

### Installation

### 1. Clone the Repository

Download the project from GitHub by running:

```bash
git clone https://github.com/johnpaultoyco-png/Motion-Detection-and-Object-Tracking-System.git
```

### 2. Open the Project Folder

```bash
cd Motion-Detection-and-Object-Tracking-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install the Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Application

```bash
python motion_detection.py
```

**Note:** Replace `motion_detection.py` with your actual Python filename if it is different.
