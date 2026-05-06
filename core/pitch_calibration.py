import numpy as np

class PitchProjection:
    def __init__(self, keypoints):
        # FIFA Standard Pitch: 105m x 68m
        # We map the 18-yard box (40.32m x 16.5m) as our anchor
        self.src_pts = np.array(keypoints, dtype="float32")
        self.dst_pts = np.array([[0, 0], [4032, 0], [4032, 1650], [0, 1650]], dtype="float32")
        self.M = cv2.getPerspectiveTransform(self.src_pts, self.dst_pts)

    def get_shot_power(self, ball_velocity_px, fps):
        """Converts pixel speed to km/h using pitch homography."""
        # Logic: 1 pixel on the 4K feed != 1 meter due to perspective
        real_velocity = self.transform_velocity(ball_velocity_px) 
        return real_velocity * 3.6 # km/h
