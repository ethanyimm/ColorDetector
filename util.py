import numpy as np
import cv2

def get_limits(color):
    
    # Convert the RGB color to HSV
    c = np.uint8([[color]]) 
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Handle special cases for black and orange
    if color == [0, 0, 0]:  # Black
        lowerLimit = np.array([0, 0, 0], dtype=np.uint8)
        upperLimit = np.array([180, 255, 30], dtype=np.uint8)  # Black has low V
    else:
        lowerLimit = hsvC[0][0][0] - 10, 100, 100  # Lower limit
        upperLimit = hsvC[0][0][0] + 10, 255, 255  # Upper limit

    # Ensure limits are within valid HSV ranges
    lowerLimit = np.clip(lowerLimit, 0, [180, 255, 255])  # H range is 0-180, others 0-255
    upperLimit = np.clip(upperLimit, 0, [180, 255, 255])

    # Convert to uint8 for OpenCV
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

