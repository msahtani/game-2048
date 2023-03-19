import pygame
from constants import *
from window  import *
from events import check_event

pygame.init()
pygame.display.set_mode((1150, 600))
pygame.display.set_caption("2048 Game")
Window.switch()
clock = pygame.time.Clock()

while True:
    check_event()
    clock.tick(FPS)
    Window.draw_window()