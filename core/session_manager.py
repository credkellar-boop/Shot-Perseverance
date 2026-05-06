def auto_filter_highlights(action_data):
    # Only save 4K cinematic clips for shots with Perfection > 85%
    if action_data['perfection_score'] > 85:
        save_to_highlight_reel(action_data['clip_path'])
    
    # Always save raw data to JSON for the reboot-resilience
    checkpoint_state(action_data)
