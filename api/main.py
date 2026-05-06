import cv2
import time
from core.pose_estimator import PoseEngine
from core.projection import ProjectionEngine
from core.classifier import ActionTrigger
from core.visuals import CinematicRenderer
from core.report_gen import ShotPerseveranceReport
from core.session_manager import SessionLogger, recover_state

class ShotPerseveranceOS:
    def __init__(self, video_source, calibration_points):
        self.cap = cv2.VideoCapture(video_source)
        self.engine = PoseEngine()
        self.matrix = ProjectionEngine(calibration_points)
        self.classifier = ActionTrigger(fps=self.cap.get(cv2.CAP_PROP_FPS))
        self.renderer = CinematicRenderer()
        self.logger = SessionLogger()
        self.session_actions = []

    def run(self):
        print("🚀 Shot-Perseverance Engine Online...")
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret: break

            # 1. AI SKELETAL TRACKING
            landmarks = self.engine.get_landmarks(frame)
            
            if landmarks:
                # 2. PHYSICS & ACTION CLASSIFICATION
                # Logic: Is it a shot? A dunk? A fast break?
                state = self.classifier.detect_state(landmarks)
                
                # 3. CINEMATIC RENDERING (The 4K "Look")
                # Logic: Draw 'Sync-Links' for Assists or 'Heat Maps' on floor
                frame = self.renderer.apply_effects(frame, landmarks, state)
                
                # 4. DATA LOGGING (Auto-Save Heartbeat)
                if state != "IDLE":
                    action_data = self.process_action_data(state, landmarks)
                    self.session_actions.append(action_data)
                    self.logger.log_event(state, action_data['score'])

            cv2.imshow('Shot-Perseverance 4K HD View', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break

        self.shutdown()

    def shutdown(self):
        # 5. FINAL REPORT GENERATION
        print("📊 Session Ended. Generating Scouting Report...")
        report = ShotPerseveranceReport(session_id=int(time.time()))
        report.generate_pdf(player_name="Elite Trainee", actions=self.session_actions)
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # In a real reboot scenario, 'recover_state()' would pull these from the .tmp file
    calib_pts = [[100, 500], [900, 500], [950, 800], [50, 800]] 
    app = ShotPerseveranceOS(video_source="data/raw_videos/practice_clip.mp4", 
                             calibration_points=calib_pts)
    app.run()
    state = recover_state()
    
    # 2. Initialize the Matrix (using saved calibration)
    # This ensures the 'Heat Map' stays aligned even after a crash
    floor_engine = ProjectionEngine(state['calibration_points'])
    
    # 3. Start Processing 4K Feed
    while True:
        # Process frames, apply 'Sync-Link' for Alley-oops, 
        # and project Heat Maps to the floor...
        pass
from core.audio_feedback import SoundEngine

class ShotPerseveranceOS:
    def __init__(self, video_source, calibration_points):
        # ... previous initializations ...
        self.audio = SoundEngine()
        self.last_state = "IDLE"

    def run(self):
        while self.cap.isOpened():
            # ... capture frame and landmarks ...
            state = self.classifier.detect_state(landmarks)

            # AUDIO TRIGGER LOGIC
            if state != self.last_state:
                if state == "GATHER_PHASE":
                    self.audio.play("setup")
                elif state == "SHOT_EXECUTION":
                    # Check 'Perfection' math from kinematics.py
                    if self.kinematics.get_score() > 90:
                        self.audio.play("perfect_release")
                
                self.last_state = state

            # ... render and log ...
def apply_focus_zoom(frame, landmarks, zoom_factor=1.2):
    """
    Digitally zooms into the player's 'Shooting Pocket' during Focus.
    """
    h, w = frame.shape[:2]
    # Center the crop on the Mid-Hip landmark
    center_x, center_y = landmarks[24].x * w, landmarks[24].y * h
    
    # Calculate crop boundaries
    new_w, new_h = w / zoom_factor, h / zoom_factor
    x1, y1 = int(center_x - new_w/2), int(center_y - new_h/2)
    
    # Crop and resize back to 4K
    cropped = frame[max(0,y1):int(y1+new_h), max(0,x1):int(x1+new_w)]
    return cv2.resize(cropped, (w, h))
