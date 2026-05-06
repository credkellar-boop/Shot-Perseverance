class SportKernel:
    def __init__(self, sport_type):
        self.sport = sport_type
        self.physics = self.load_physics_module()

    def load_physics_module(self):
        # Logic: Swap gravity constants and collision detection
        if self.sport == "HOCKEY":
            return {"friction": 0.02, "object": "PUCK"}
        elif self.sport == "BASEBALL":
            return {"friction": 0.5, "object": "BALL_9IN"}
        elif self.sport == "UFC":
            return {"mode": "CONTACT_DYNAMICS"}
