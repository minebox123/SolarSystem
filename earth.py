import pygame
import math


class Earth:
    """Earth planet"""

    def __init__(self, main):
         # main settings
        self.surface = main.screen
        self.settings = main.settings
        self.sun_center = main.rect.center[0]

        # Mercury attributes
        self.color = self.settings.earth_color
        self.radius = self.settings.earth_radius
        self.dist_from_sun = 150
        # self.x = self.sun_center + 100 + self.dist_from_sun
        # self.y = 600
        self.x = 1050
        self.y = 350

        self.radians = 0
        self.velocity = 0.05

    def draw(self):
        pygame.draw.circle(self.surface, self.color,
                           (self.x, self.y), self.radius)

    def move(self):
        self.radians += self.velocity
        self.x = self.x + math.cos(self.radians) * 10
        self.y = self.y + math.sin(self.radians) * 10
