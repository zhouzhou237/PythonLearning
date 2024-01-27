import sys

import pygame


def check_events():
    # monitor the keyboard abd mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """renew the images in screen and shift th the new screen"""

    # background color
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # let the window visible
    pygame.display.flip()
