import pytest
import numpy as np
from core.pose_estimator import PoseEngine

def test_engine_initialization():
    """Verify the AI model loads without crashing the OS."""
    engine = PoseEngine()
    assert engine is not None

def test_frame_processing():
    """Verify the engine can process a raw image array."""
    engine = PoseEngine()
    # Create a blank 640x480 image
    fake_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    results = engine.get_landmarks(fake_frame)
    # The build passes if this executes without error
    assert results is not None
