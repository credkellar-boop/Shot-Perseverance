import pygame

class SoundEngine:
    def __init__(self):
        pygame.mixer.init()
        # Pre-load sounds for 0ms latency during the 4K render
        self.sounds = {
            "setup": pygame.mixer.Sound("data/audio/beep_low.wav"),    # The 'Dip'
            "perfect_release": pygame.mixer.Sound("data/audio/swish.wav"), # 90%+ Perfection
            "off_rhythm": pygame.mixer.Sound("data/audio/clank.wav"),     # Shot too slow/fast
            "shot_clock": pygame.mixer.Sound("data/audio/buzzer.wav")     # Time limit for fast break
        }

    def play(self, event_name):
        if event_name in self.sounds:
            self.sounds[event_name].play()
