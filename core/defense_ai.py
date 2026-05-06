def spectacular_offensive_filter(play_data):
    """
    Only triggers 4K Auto-Save for Offense if:
    1. Distance > 20 yards
    2. Vertical Jump > 30 inches (Spectacular Catch)
    3. Ball velocity > 55mph (Bullet Pass)
    4. Proximity to Endzone < 1 yard (Score)
    """
    if play_data['yards_gained'] > 20 or play_data['is_touchdown']:
        return "SPECTACULAR_PLAY"
    return "LOG_ONLY" # Saves data points but not the 4K clip
