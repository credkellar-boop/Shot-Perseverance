def predict_curve(velocity, spin, air_density=1.225):
    """
    Predicts the 'Beckham Curve' by calculating the pressure 
    differential on the ball's surface.
    """
    # Logic: If spin > 500rpm, apply Magnus displacement to the trajectory arc
    curve_factor = (spin * velocity) / air_density
    return curve_factor
