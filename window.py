from constant import *
from load_game import get_grid
import pygame
from utils import *

pygame.init()
font = pygame.font.Font('assets/fonts/SpaceMission.otf', FONT_SIZE)

def draw_window(screen):
    screen.fill(hex_to_rgb('#FAF8EF'))

    pygame.draw.rect(
        screen,
        hex_to_rgb("#BBADA0"),
        pygame.Rect(50, 50, 500, 500),
        border_radius= 10
    )

    game = get_grid()
    if not game: return

    it = iter(game)
    for i in range(16):
        W = 115
        P = 10
        X = 55 + (W + P)*(i%4)
        Y = 55 + (W + P)*(i//4)
        n = next(it)
        r = pygame.draw.rect(
            screen, GRID_COLORS[n],
            pygame.Rect(X, Y, W, W),
            border_radius= 10
        )
        
        if n != 0:
            text = font.render(str(int(n)), True, (0,0,0))
            screen.blit(text, center(r, text))
    pygame.display.update()