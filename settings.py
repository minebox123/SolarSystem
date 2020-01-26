import pygame


class Settings:
    """Contains all the simulation parameters"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.screen_color = (0, 0, 0)

        # The sun parameters
        self.sun_radius = 10.0
        self.sun_color = (255, 255, 102)