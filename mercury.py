import pygame


class Mercury:
    """Mercury planet"""

    def __init__(self, main):
         # main settings
        self.surface = main.screen
        self.settings = main.settings

        # Mercury attributes
        self.color = self.settings.mercury_color
        self.radius = self.settings.mercury_radius
        self.center = (1000, 600)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
