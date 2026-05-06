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
