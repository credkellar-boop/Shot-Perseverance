import numpy as np
import cv2

class OffsideEngine:
    def __init__(self, pitch_matrix):
        self.matrix = pitch_matrix

    def get_offside_line(self, players, team_id):
        """
        Logic:
        1. Filter for all players on the defending team.
        2. Find the 2nd to last defender (including the keeper).
        3. Project their X-coordinate into the 3D pitch space.
        """
        defenders = [p for p in players if p.team == team_id]
        # Sort by distance to their own goal
        defenders.sort(key=lambda p: p.x_coord) 
        
        if len(defenders) >= 2:
            last_man = defenders[1] # The 'Offside' anchor
            return last_man.x_coord
        return None

    def check_violation(self, strikers, offside_line_x):
        """Returns True if any part of a striker is past the line."""
        for s in strikers:
            if s.x_coord > offside_line_x:
                return True, s.id
        return False, None
