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
def apply_nfl_visuals(frame, play_state, is_defense=True):
    # DEFENSE: Always draw tactical overlays
    if is_defense:
        frame = draw_coverage_bubbles(frame)
        frame = draw_pass_rush_timer(frame)
        
    # OFFENSE: Only draw if the play is 'Spectacular'
    else:
        if play_state == "SPECTACULAR":
            frame = apply_speed_streaks(frame) # Neon trails on the runner
            frame = trigger_zoom_on_ball(frame) # 4K crop on the catch
            
    return frame
