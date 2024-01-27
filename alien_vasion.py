import sys
import pygame


def run_game():
    # Initialise the game and create a screen
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Start the main cycle of game
    while True:

        # monitor the keyboard abd mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # let the window visible
        pygame.display.flip()


run_game()
