import pygame


class Mercury:
    """Mercury planet"""

    def __init__(self, main):
         # main settings
        self.surface = main.screen
        self.settings = main.settings
        self.sun_center = main.rect.center[0]

        # Mercury attributes
        self.color = self.settings.mercury_color
        self.radius = self.settings.mercury_radius
        self.dist_from_sun = 58
        self.center = (self.sun_center + 100 + self.dist_from_sun, 600)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
