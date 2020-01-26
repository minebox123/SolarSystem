import pygame


class Settings:
    """Contains all the simulation parameters"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 1200
        self.screen_color = (0, 0, 0)

        self.au = 0.0

        # The sun parameters
        self.sun_radius = 100.0
        self.sun_color = (255, 255, 102)
        self.diameter = 1392684.0

        # Mercury params
        self.merc_diameter = 4979.4
        self.mercury_radius = self.sun_radius * 3 / (
            self.diameter / self.merc_diameter)
        self.mercury_color = (128, 128, 128)
