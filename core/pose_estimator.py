import cv2
import mediapipe as mp

class PoseEngine:
    def __init__(self):
        # Fix: Direct access to Pose to avoid 'solutions' attribute issues in CI
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.7)

    def get_landmarks(self, frame):
        if frame is None:
            return None
        results = self.pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return results
