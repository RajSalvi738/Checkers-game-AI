import pygame

#window size
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

#Board constants
ROWS, COLS = 8, 8
SQUARE_SIZE = SCREEN_WIDTH // COLS

#colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))
