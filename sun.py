import pygame


class Sun:
    """The sun"""

    def __init__(self, main):
        # main settings
        self.surface = main.screen
        self.settings = main.settings

        # Sun attributes
        self.color = self.settings.sun_color
        self.radius = self.settings.sun_radius
        self.center = main.rect.center

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
