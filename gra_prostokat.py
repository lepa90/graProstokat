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
            self._update_prostokat()
    def _update_prostokat(self):

        self._check_flet_edges()
        self.prostokat.update()




    def _check_flet_edges(self):

        if self.prostokat.rect1.top < 0 or self.prostokat.rect1.bottom > 800:
            self._changes_fleet_direction()




    def _changes_fleet_direction(self):

        self.settings.flet_direction *= -1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.prostokat.wys_pros()
        pygame.display.flip()

if __name__ == '__main__':
    gp = Gra_Prostokat()
    gp.run_game()