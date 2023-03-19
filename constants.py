# colors
import pygame

from UI import hex_to_rgb


WHITE = 255, 255, 255
RED = 255, 0, 0
BLACK = 0, 0, 0
MARRON = hex_to_rgb('#8f7a66')
LIGHT_YELLOW = hex_to_rgb('#FAF8EF')
LIGHT_MARRON = hex_to_rgb("#BBADA0")

# display size
WIDTH, HEIGHT = 600, 600
DISP_SIZE = WIDTH, HEIGHT

#Frames per second
FPS = 30

GRID_COLORS = {
    0 :    (204, 192, 179),
    2 :    (238, 228, 218),
    4 :    (237, 224, 200),
    8 :    (242, 177, 121),
    16 :   (245, 149, 99),
    32 :   (246, 124, 95),
    64 :   (246, 94, 59),
    128 :  (237, 207, 114),
    256 :  (237, 204, 97),
    512 :  (237, 200, 80),
    1024 : (237, 197, 63),
    2048 : (237, 194, 46),
}

ARROWS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]