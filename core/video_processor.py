def get_cinematic_speed(current_frame, release_frame, window=30):
    """
    Returns the delay factor. 
    1.0 = Normal speed
    0.2 = 5x Slow motion
    """
    distance = abs(current_frame - release_frame)
    
    if distance < 5:
        return 0.2  # The "Freeze Frame" release moment
    elif distance < window:
        # Smooth transition to slow-mo
        return 0.2 + (0.8 * (distance / window))
    return 1.0
