import pygame
import sys

from settings import Settings
from sun import Sun
from mercury import Mercury
from jupiter import Jupiter
from earth import Earth


class SolarSystem:
    """Run the whole solar system"""

    def __init__(self):
        pygame.init()

        # classes
        self.settings = Settings()

        # Screen config
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.caption = pygame.display.set_caption("Solar System")
        self.rect = self.screen.get_rect()

        self.sun = Sun(self)
        self.mercury = Mercury(self)
        self.jupiter = Jupiter(self)
        self.earth = Earth(self)

    def main(self):

        while True:

            self.screen.fill((0, 0, 0))

            # Astronomical Objects
            self.astro_objects()

            self.screen_config()
            # user interaction
            self._key_pressed()

    def screen_config(self):

        pygame.display.update()

    def _key_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def astro_objects(self):
        self.mercury.draw()
        self.sun.draw()
        self.jupiter.draw()
        self.earth.draw()
        self.earth.move()


if __name__ == "__main__":
    sol_sys = SolarSystem()
    sol_sys.main()
