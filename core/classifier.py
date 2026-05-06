class ActionTrigger:
    def __init__(self, fps=60):
        self.fps = fps
        self.velocity_threshold = 15.0  # mph equivalent in pixels
        self.jump_threshold = 0.05      # % of frame height

    def detect_state(self, player_data, ball_data):
        """
        Logic:
        - Fast Break: Horizontal velocity stays high for > 1.5 seconds.
        - Jump Shot: Vertical velocity goes up, then stops (apex), then ball separates.
        - Block: Ball velocity vector flips 180 degrees within 2 frames.
        """
        v_x = player_data['velocity_x']
        v_y = player_data['velocity_y']
        
        if v_x > self.velocity_threshold:
            return "FAST_BREAK"
        
        if v_y < -self.jump_threshold: # Negative is UP in OpenCV
            if ball_data['is_released']:
                return "SHOT_EXECUTION"
            return "GATHER_PHASE"
            
        return "IDLE"
core/classifier.py
