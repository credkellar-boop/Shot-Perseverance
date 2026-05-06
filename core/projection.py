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
