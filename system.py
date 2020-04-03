import pygame
import sys
import os

from celestial_object import Celestial_object
from object_settings import Object_settings


class System:
    pygame.init()

    def __init__(self):
        self.width = 2500
        self.height = 1200
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Solar system")
        self.bg = (0, 0, 0)
        self.fps = pygame.time.Clock()
        self.settings = Object_settings()

        # Create instances of celestial objects
        self.sun = Celestial_object(self.window, self.settings.sun_color,
                                    self.settings.sun_X, self.settings.sun_Y, self.settings.sun_radius, None)

        # Mercury's system
        self.mercury = Celestial_object(self.window, self.settings.mercury_color,
                                        self.settings.mercury_X, self.settings.mercury_Y, self.settings.mercury_radius, self.settings.mercury_speed)

        # Venus system
        self.venus = Celestial_object(self.window, self.settings.venus_color,
                                      self.settings.venus_X, self.settings.venus_Y, self.settings.venus_radius, self.settings.venus_speed)

        self.earth = Celestial_object(self.window, self.settings.earth_color,
                                      self.settings.earth_X, self.settings.earth_Y, self.settings.earth_radius, self.settings.earth_speed)

        self.mars = Celestial_object(self.window, self.settings.mars_color,
                                     self.settings.mars_X, self.settings.mars_Y, self.settings.mars_radius, self.settings.mars_speed)

        # Jupiter's system
        self.jupiter = Celestial_object(self.window, self.settings.jupiter_color,
                                        self.settings.jupiter_X, self.settings.jupiter_Y, self.settings.jupiter_radius, self.settings.jupiter_speed)
        # self.europa = Celestial_object(self.window, self.settings.satellite_color,
        #                                self.settings.jupiter_X + 20, self.settings.jupiter_Y, self.settings.jupiter_radius // 50)

        # Saturn's system
        self.saturn = Celestial_object(self.window, self.settings.saturn_color,
                                       self.settings.saturn_X, self.settings.saturn_Y, self.settings.saturn_radius, self.settings.saturn_speed, True)

        # Uranus system
        self.uranus = Celestial_object(self.window, self.settings.uranus_color,
                                       self.settings.uranus_X, self.settings.uranus_Y, self.settings.uranus_radius, self.settings.uranus_speed)

        # Neptune's system
        self.neptune = Celestial_object(self.window, self.settings.neptune_color,
                                        self.settings.neptune_X, self.settings.neptune_Y, self.settings.neptune_radius, self.settings.neptune_speed)

    def main(self):
        run = True
        while run:
            self.fps.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # draw all celestial objects
            self.draw_celestial_objects()

            # window settings
            self.window_setup()

    def window_setup(self):
        pygame.display.flip()
        self.window.fill(self.bg)

    def draw_celestial_objects(self):
        self.sun.draw_object()

        sunX = self.settings.sun_X
        sunY = self.settings.sun_Y

        # Mercury
        self.mercury.draw_object()
        self.mercury.move_object(self.settings.mercury_X - sunX, sunX, sunY)

        # Venus
        self.venus.draw_object()
        self.venus.move_object(self.settings.venus_X - sunX, sunX, sunY)

        # Earth
        self.earth.draw_object()
        self.earth.move_object(self.settings.earth_X - self.settings.sun_X,
                               self.settings.sun_X, self.settings.sun_Y)
        self.earth.draw_satellite(self.settings.earth_radius)
        self.earth.move_satellite(
            self.settings.earth_X, self.settings.earth_Y, 10)

        # Mars
        self.mars.draw_object()
        self.mars.move_object(self.settings.mars_X - self.settings.sun_X,
                              self.settings.sun_X, self.settings.sun_Y)

        # Jupiter's system
        self.jupiter.draw_object()
        self.jupiter.move_object(self.settings.jupiter_X - self.settings.sun_X,
                                 self.settings.sun_X, self.settings.sun_Y)
        self.jupiter.draw_satellite(self.settings.jupiter_radius)
        self.jupiter.move_satellite(
            self.settings.jupiter_X, self.settings.jupiter_Y, 20)

        # Saturn's system
        self.saturn.draw_object()
        self.saturn.move_object(
            self.settings.saturn_X - self.settings.sun_X, self.settings.sun_X, self.settings.sun_Y)

        # Uranus system
        self.uranus.draw_object()
        self.uranus.move_object(self.settings.uranus_X - self.settings.sun_X,
                                self.settings.sun_X, self.settings.sun_Y)

        # Neptune system
        self.neptune.draw_object()
        self.neptune.move_object(self.settings.neptune_X - self.settings.sun_X,
                                 self.settings.sun_X, self.settings.sun_Y)


if __name__ == "__main__":
    system = System()
    system.main()
