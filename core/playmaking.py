class PlaymakingEngine:
    def __init__(self):
        self.passer_id = None
        self.finisher_id = None

    def detect_alley_oop(self, ball_pos, players):
        """
        Criteria:
        1. Ball is in a high-arc lob (Parabolic check).
        2. Finisher's Hip Y-coordinate is decreasing (Jumping).
        3. Catch occurs above Rim Height.
        """
        for p_id, p_data in players.items():
            if p_data['is_jumping'] and ball_pos['y'] < p_data['hand_y']:
                return True, p_id
        return False, None
