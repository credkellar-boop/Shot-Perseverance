def draw_sync_link(frame, passer_pos, finisher_pos, alpha=0.6):
    """
    Renders a glowing neon line between two players during a lob.
    """
    overlay = frame.copy()
    # Draw the line with a 'Neon Cyan' color
    cv2.line(overlay, passer_pos, finisher_pos, (255, 255, 0), 8, cv2.LINE_AA)
    
    # Apply a light blur to the line to create a 'Glow' effect
    overlay = cv2.GaussianBlur(overlay, (7, 7), 0)
    
    # Blend with original frame for translucency
    return cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
