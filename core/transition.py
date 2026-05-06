class TransitionEngine:
    def track_fast_break(self, player_positions, fps):
        """
        Calculates 'Lane Efficiency'. 
        Measures the distance covered over time during a change of possession.
        """
        for p_id, pos_history in player_positions.items():
            # Calculate horizontal velocity (mph/kph)
            dx = pos_history[-1][0] - pos_history[-5][0]
            velocity = (abs(dx) * fps) * self.scale_factor
            
            if velocity > 15: # Threshold for a 'Sprinting' state
                self.apply_motion_trails(p_id)
