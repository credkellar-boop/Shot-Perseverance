import cv2
from fastapi import FastAPI
from core.pose_estimator import PoseEngine
from core.classifier import ActionTrigger
from core.visuals import CinematicRenderer
from .logger import SessionLogger

app = FastAPI()

class ShotPerseveranceOS:
    def __init__(self, video_source=0, calibration_points=None):
        self.cap = cv2.VideoCapture(video_source)
        self.engine = PoseEngine()
        self.classifier = ActionTrigger(fps=self.cap.get(cv2.CAP_PROP_FPS))
        self.renderer = CinematicRenderer()
        self.logger = SessionLogger()

    def run(self):
        print("🏀 Shot-Perseverance OS Online...")
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret: break

            landmarks = self.engine.get_landmarks(frame)
            if landmarks:
                # Logic: Is it a shot? A dunk?
                state = self.classifier.detect_state(landmarks)
                self.renderer.apply_effects(frame, landmarks, state)

        self.cap.release()

# Instantiate the OS
os_kernel = ShotPerseveranceOS()

@app.get("/")
def status():
    return {"status": "Kernel Active", "version": "1.0.0"}

@app.post("/run")
def start_processing():
    os_kernel.run()
    return {"message": "Processing Complete"}
