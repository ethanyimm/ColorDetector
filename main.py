import cv2
from PIL import Image
import numpy as np
from util import get_limits  # Import the get_limits function from util.py

# Define color ranges in RGB
colors = {
    'yellow': [0, 255, 255],
    'green': [0, 255, 0],
    'blue': [255, 0, 0],
}

def detect_colors():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        # Convert the frame to HSV colorspace
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Iterate through each color and create a mask
        for color_name, rgb_value in colors.items():
            lowerLimit, upperLimit = get_limits(rgb_value)

            # Create mask for each color
            mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

            # Convert mask to PIL Image for bounding box detection
            mask_ = Image.fromarray(mask)
            bbox = mask_.getbbox()

            # Draw bounding boxes if contours are found
            if bbox is not None:
                x1, y1, x2, y2 = bbox
                frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, color_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Show the frame with bounding boxes
        cv2.imshow('frame', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Start the color detection
if __name__ == "__main__":
    detect_colors()
