import cv2
import numpy as np

class PerspectiveManager:
    def __init__(self, src_pts):
        # src_pts: The 4 pixels you clicked in calibration
        # dst_pts: The actual dimensions of an NBA paint (in pixels for a top-down view)
        self.dst_pts = np.array([[0, 0], [480, 0], [480, 570], [0, 570]], dtype="float32")
        self.src_pts = np.array(src_pts, dtype="float32")
        self.M = cv2.getPerspectiveTransform(self.src_pts, self.dst_pts)
        self.Minv = cv2.getPerspectiveTransform(self.dst_pts, self.src_pts)

    def pixel_to_court(self, x, y):
        """Converts a person's foot pixel to a (lat, long) on the court."""
        point = np.array([[[x, y]]], dtype="float32")
        transformed = cv2.perspectiveTransform(point, self.M)
        return transformed[0][0]

    def draw_floor_graphic(self, frame, overlay_img):
        """Warps a graphic (like a Heat Map) onto the video floor."""
        warped = cv2.warpPerspective(overlay_img, self.Minv, (frame.shape[1], frame.shape[0]))
        return cv2.addWeighted(frame, 1.0, warped, 0.5, 0)
import cv2
import numpy as np

class ProjectionEngine:
    """
    This class handles 'The Matrix'. It converts pixels (x, y) 
    into real-world court coordinates (meters/feet).
    """
    def __init__(self, calibration_data):
        # calibration_data comes from your click-event tool
        self.src_pts = np.array(calibration_data, dtype="float32")
        
        # Standard NBA Paint Dimensions (mapped to a 1000x1000 grid for math)
        self.dst_pts = np.array([[0, 0], [1000, 0], [1000, 1000], [0, 1000]], dtype="float32")
        
        # The 'Secret Sauce': The Homography Matrix
        self.matrix = cv2.getPerspectiveTransform(self.src_pts, self.dst_pts)

    def get_real_world_velocity(self, pos1, pos2, fps):
        """
        Calculates ACTUAL speed in MPH by projecting pixels to the floor first.
        """
        p1 = self.transform_point(pos1)
        p2 = self.transform_point(pos2)
        dist = np.linalg.norm(p1 - p2)
        return (dist * fps) * 2.237 # Conversion to MPH
