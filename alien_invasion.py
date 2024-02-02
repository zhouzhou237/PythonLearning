import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialise the game and create a screen
    pygame.init()
    ai_Settings = Settings()
    screen = pygame.display.set_mode((ai_Settings.screen_width, ai_Settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # add ship to the screen
    ship = Ship(screen)

    # Start the main cycle of game
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_Settings, screen, ship)


run_game()
