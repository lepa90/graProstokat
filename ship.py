import pygame

class Ship:
    def __init__(self, gp_game):
        super().__init__()
        self.screen = gp_game.screen
        self.screen_rect = gp_game.screen.get_rect()
        self.settings = gp_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.y = 400
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False



    def update(self):
        if self.moving_right:
            self.y += self.settings.ship_speed
        if self.moving_left:
            self.y -= self.settings.ship_speed
        self.rect.y = self.y
    def blitme(self):
        self.screen.blit(self.image, self.rect)

