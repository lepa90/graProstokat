import pygame

class Ship:
    def __init__(self, gp_game):
        self.screen = gp_game.screen
        self.screen_rect = gp_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.y = 400
    def blitme(self):
        self.screen.blit(self.image, self.rect)

