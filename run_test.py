import pytest
import cv2
import numpy as np
from core.pose_estimator import PoseEngine

def test_engine_initialization():
    # Test if the engine can initialize without crashing
    engine = PoseEngine()
    assert engine is not None

def test_mock_frame_processing():
    engine = PoseEngine()
    # Create a blank black image to simulate a video frame
    fake_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    results = engine.get_landmarks(fake_frame)
    
    # The test passes if the function executes, even if no landmarks are found in a black image
    assert hasattr(results, 'pose_landmarks')
