# Rectangle Detector
## Overview
This project implements a real-time rectangle and square detection system using OpenCV. It applies Gaussian blur, Canny edge detection, and contour finding to detect shapes in video captured from a webcam. The program also uses a simple Tkinter GUI to display the video stream and the results of the detection.

## Prerequisites
Python 3.x
OpenCV
NumPy
Tkinter
PIL (Python Imaging Library)
You can install the necessary libraries using pip:

bash
Copy code
pip install opencv-python numpy pillow
## Usage
To run the program, simply execute the python file in your terminal:

bash
Copy code
python rectangle_detector.py
## Functionality
This program takes video input from a webcam and processes each frame to detect rectangles and squares. Detected rectangles and squares are highlighted on the video and their width and height in pixels are displayed on screen.

## Limitations and Future Work
The current implementation has a simple detection algorithm and might not perfectly detect all rectangles and squares. Future versions of this project may use machine learning or other advanced techniques to improve detection accuracy.

## License
This project is licensed under the terms of the MIT license.

