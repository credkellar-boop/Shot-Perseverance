import cv2
import numpy as np
import yaml

class CourtCalibrator:
    def __init__(self):
        self.points = []

    def click_event(self, event, x, y, flags, params):
        # Store the (x, y) pixel coordinates when the mouse is clicked
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append([x, y])
            print(f"Point Registered: {x}, {y}")

    def get_calibration(self, image_path):
        img = cv2.imread(image_path)
        cv2.imshow("Calibration: Click 4 Corners of the Paint", img)
        cv2.setMouseCallback("Calibration: Click 4 Corners of the Paint", self.click_event)
        
        # Wait for 4 clicks then press any key
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save these coordinates to your config.yaml
        return self.points

# Logic: We map these 4 pixels to real-world meters (e.g., 16ft x 19ft for the paint)
