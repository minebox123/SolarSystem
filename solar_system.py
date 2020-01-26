import pygame
import sys

from settings import Settings


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

    def main(self):
        while True:
            self.screen_config()

            # user interaction
            self._key_pressed()

    def screen_config(self):
        self.screen.fill(self.settings.screen_color)
        pygame.display.update()

    def _key_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


if __name__ == "__main__":
    sol_sys = SolarSystem()
    sol_sys.main()