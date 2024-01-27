import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen

        # load ship.bmp and achieve its size
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set the ship in the bottom middle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # draw the ship in the right place
        self.screen.blit(self.image, self.rect)
