import pygame


class Jupiter:
    """Jupiter planet"""

    def __init__(self, main):
         # main settings
        self.surface = main.screen
        self.settings = main.settings
        self.sun_center = main.rect.center[0]

        # Mercury attributes
        self.color = self.settings.jupiter_color
        self.radius = self.settings.jupiter_radius
        self.dist_from_sun = 778
        self.center = (self.sun_center + 100 + self.dist_from_sun, 600)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
