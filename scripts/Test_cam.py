#!/usr/bin/env -S uv run --script

from cv_bridge import CvBridge
import cv2

def main():
    # Initialize webcam
    cam = VideoCapture(0)
    # Capture one frame
    ret, frame = cam.read()

    if ret:
      imshow("Captured", frame)         
      imwrite("/home/user/Pictures/scene.png", frame)  
      waitKey(0)                      
      destroyWindow("Captured")       
    else:
      print("Failed to capture image.")

    cam.release()

if __name__ == "__main__":
    main()
