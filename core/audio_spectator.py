import numpy as np

class CrowdWowDetector:
    def __init__(self, threshold_db=25):
        self.threshold = threshold_db # Increase in decibels above baseline

    def is_spectacular_audio(self, audio_data):
        # Calculate Root Mean Square (RMS) to find volume
        rms = np.sqrt(np.mean(audio_data**2))
        db = 20 * np.log10(rms) if rms > 0 else 0
        
        # Logic: If noise spikes 25dB above the 10-second rolling average
        if db > self.baseline_db + self.threshold:
            return True
        return False
