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

        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # draw the ship in the right place
        self.screen.blit(self.image, self.rect)
