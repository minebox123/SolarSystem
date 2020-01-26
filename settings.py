import pygame


class Settings:
    """Contains all the simulation parameters"""

    def __init__(self):
        # Screen settings
        self.screen_width = 2000
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

        # Jupiter params
        self.jupiter_diameter = 142984.0
        self.jupiter_radius = self.sun_radius * 3 / \
            (self.diameter / self.jupiter_diameter)
        self.jupiter_color = (51, 51, 51)
