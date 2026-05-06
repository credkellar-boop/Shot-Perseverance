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
