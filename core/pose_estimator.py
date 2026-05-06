import cv2
import mediapipe as mp

class PoseEngine:
    def __init__(self):
        # Using a more resilient initialization to avoid 'AttributeError'
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_landmarks(self, frame):
        if frame is None:
            return None
        # MediaPipe requires RGB; OpenCV uses BGR
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb_frame)
