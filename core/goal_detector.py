class GoalDetector:
    def __init__(self, goal_corners):
        # Coordinates of the posts and crossbar from calibration
        self.goal_plane = goal_corners 

    def is_goal(self, ball_pos):
        """
        Checks if the center of the ball has completely crossed 
        the vertical plane between the posts.
        """
        if self.ball_crossed_plane(ball_pos):
            if self.is_within_posts(ball_pos):
                return True
        return False
