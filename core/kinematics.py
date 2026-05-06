import numpy as np

class ShotPhysics:
    @staticmethod
    def calculate_release_height(wrist_y, floor_y, scale_factor=1.0):
        """Calculates height in feet/meters based on pixel scale."""
        return (floor_y - wrist_y) * scale_factor

    @staticmethod
    def calculate_velocity(positions, fps):
        """Calculates instantaneous velocity between frames."""
        if len(positions) < 2: return 0
        dist = np.linalg.norm(np.array(positions[-1]) - np.array(positions[-2]))
        return dist * fps
import numpy as np

def calculate_angle(a, b, c):
    a = np.array(a) # Shoulder
    b = np.array(b) # Elbow
    c = np.array(c) # Wrist
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360-angle
    return angle
