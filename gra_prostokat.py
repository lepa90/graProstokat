import sys

import pygame
from settings import Settings
from ship import Ship
from prostokat import Prostokat

class Gra_Prostokat:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(( self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Gra Prostokat")
        self.ship = Ship(self)
        self.prostokat = Prostokat(self)


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.prostokat.update()




    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.prostokat.wys_prze()
        pygame.display.flip()

if __name__ == '__main__':
    gp = Gra_Prostokat()
    gp.run_game()