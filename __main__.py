import pygame
from constant import *
from events import check_events
from game_logic import Game2048
from load_game import load_game
from window import draw_window

game = load_game()

screen = pygame.display.set_mode(DISP_SIZE)
pygame.display.set_caption("2048 Game")

clock = pygame.time.Clock()

while True:
    check_events()
    clock.tick(FPS)
    draw_window(screen)
    