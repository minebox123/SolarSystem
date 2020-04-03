import pygame
import math
import pygame.gfxdraw as pen


class Celestial_object:
    """
    A parent class of all the planets and the Sun
    """

    def __init__(self, surface, color, x, y, radius, speed, rings=False):
        self.radius = radius
        self.color = color
        self.width = 0
        self.surface = surface
        self.x = x
        self.y = y
        self.vel = 0.005
        self.radians = 0
        self.satellite_radians = 0
        self.sat_x = self.x + 20
        self.sat_y = self.y
        self.rings = rings
        self.speed = speed

    def draw_object(self):
        circle = pygame.draw.circle(self.surface, self.color,
                                    (self.x, self.y), self.radius, self.width)

        if self.rings:
            pygame.draw.arc(self.surface, (108, 102, 90),
                            (circle.x - 5, circle.y - 5, circle.width + 10, circle.height + 10), 0, math.pi * 2, 3)

    def move_object(self, distance_from_sun, sun_X, sun_Y):
        self.radians += self.vel * self.speed

        self.x = int(sun_X + distance_from_sun * (math.cos(self.radians)))
        self.y = int(sun_Y - distance_from_sun * (math.sin(self.radians)))

    def draw_satellite(self, parent_planet_size):
        satellite_color = (255, 255, 255)
        satellite_radius = int(parent_planet_size / 50)
        self.satellite_radians += 1000
        pygame.draw.circle(self.surface, satellite_color,
                           (self.sat_x, self.sat_y), satellite_radius)

    def move_satellite(self, parent_planet_X, parent_planet_Y, distance_from_planet):
        self.satellite_radians += self.vel
        self.sat_x = int(self.x + distance_from_planet *
                         math.cos(self.satellite_radians))
        self.sat_y = int(self.y + distance_from_planet *
                         math.sin(self.satellite_radians))
