import sys

import pygame


def check_events(ship):
    # monitor the keyboard abd mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """renew the images in screen and shift th the new screen"""

    # background color
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # let the window visible
    pygame.display.flip()
