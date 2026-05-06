import json
import time

def auto_save_metrics(session_id, action_type, metrics):
    filename = f"data/logs/session_{session_id}.json"
    with open(filename, 'a') as f:
        json.dump({"timestamp": time.time(), "type": action_type, "data": metrics}, f)
        f.write('\n')

# REBOOT WRAPPER
if __name__ == "__main__":
    while True:
        try:
            print("Shot-Perseverance Online...")
            run_engine() # Your main processing loop
        except Exception as e:
            print(f"System Crash: {e}. Rebooting in 5 seconds...")
            time.sleep(5)
            continue # Restarts the loop automatically
import os
import signal

def emergency_save(signum, frame):
    """Triggered if the system is shutting down or crashing."""
    print("CRITICAL: Saving session data before reboot...")
    # Call your session_manager.checkpoint_state() here
    exit(1)

# Register the reboot/interrupt signals
signal.signal(signal.SIGINT, emergency_save)
signal.signal(signal.SIGTERM, emergency_save)
from core.projection import ProjectionEngine
from core.session_manager import recover_state

def run_engine():
    # 1. Check for Reboot Recovery
    state = recover_state()
    
    # 2. Initialize the Matrix (using saved calibration)
    # This ensures the 'Heat Map' stays aligned even after a crash
    floor_engine = ProjectionEngine(state['calibration_points'])
    
    # 3. Start Processing 4K Feed
    while True:
        # Process frames, apply 'Sync-Link' for Alley-oops, 
        # and project Heat Maps to the floor...
        pass
