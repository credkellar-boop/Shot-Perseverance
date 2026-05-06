def auto_filter_highlights(action_data):
    # Only save 4K cinematic clips for shots with Perfection > 85%
    if action_data['perfection_score'] > 85:
        save_to_highlight_reel(action_data['clip_path'])
    
    # Always save raw data to JSON for the reboot-resilience
    checkpoint_state(action_data)
import subprocess

def sync_to_cloud(file_path):
    """
    Uploads the 4K video and PDF report to the cloud.
    """
    # Using a simple CLI command for efficiency
    try:
        subprocess.run(["aws", "s3", "cp", file_path, "s3://my-shot-reports/"], check=True)
        print(f"Cloud Backup Success: {file_path}")
    except:
        print("Offline: Data saved locally only.")
