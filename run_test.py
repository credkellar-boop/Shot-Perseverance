import cv2
from core.pose_estimator import PoseEngine

def test_engine(video_path):
    engine = PoseEngine()
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Get landmarks from our engine
        landmarks = engine.get_landmarks(frame)
        
        if landmarks:
            # Focus on the right wrist (Landmark 16) or left (Landmark 15)
            # This is the 'release point' data we'll eventually feed to kinematics.py
            mp_drawing = mp.solutions.drawing_utils
            mp_pose = mp.solutions.pose
            mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Shot-Perseverance Debug Feed', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Drop a clip of a jumpshot into data/raw_videos/ and put the filename here
    test_engine("data/raw_videos/my_shot.mp4")
