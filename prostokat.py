import pygame

class Prostokat:
    def __init__(self, gp_game):
        super().__init__()
        self.screen = gp_game.screen

        self.settings = gp_game.settings
        self.color = self.settings.prostokat_color

        self.rect = pygame.Rect(1050, 400, self.settings.prostokat_height, self.settings.prostokat_width)

        self.y = float(self.rect.y)





    def update(self):
        self.y -=self.settings.prostokat_speed
        self.rect.y = self.y
    def wys_prze(self):
        screen_rect = pygame.draw.rect(self.screen, self.color, self.rect)
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True










