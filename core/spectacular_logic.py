class SpectacularPlayEngine:
    def __init__(self):
        self.thresholds = {
            "air_yards": 30,      # Any pass over 30 yards is 'Spectacular'
            "yac": 20,            # 20+ yards after catch
            "extension": 0.85,    # Player reaching 85% of max limb extension (diving catch)
            "velocity_delta": 15  # Sudden 15mph burst (Ankle-breaker juke)
        }

    def is_offensive_highlight(self, play_metrics):
        """
        Logic: Only returns True if the play meets 'Spectacular' criteria.
        """
        if play_metrics['touchdown']: return True
        if play_metrics['distance'] > self.thresholds['air_yards']: return True
        if play_metrics['max_extension'] > self.thresholds['extension']: return True
        
        return False
