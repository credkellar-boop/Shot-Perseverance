import pytest
import numpy as np
from core.pose_estimator import PoseEngine

def test_engine_initialization():
    engine = PoseEngine()
    assert engine is not None

def test_mock_frame_processing():
    engine = PoseEngine()
    # Create blank frame for CI testing
    fake_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    results = engine.get_landmarks(fake_frame)
    assert results is not None
