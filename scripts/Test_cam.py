#!/usr/bin/env -S uv run --script


import cv2

def main():
    # Initialize webcam
    cam = cv2.VideoCapture(0)
    # Capture one frame
    ret, frame = cam.read()

    if ret:
      #cv2.imshow("Captured", frame)         
      cv2.imwrite("/home/mrosas/Pictures/scene.png", frame)  
      #cv2.waitKey(0)                      
      #cv2.destroyAllWindows()       
    else:
      print("Failed to capture image.")

    cam.release()

if __name__ == "__main__":
    main()
