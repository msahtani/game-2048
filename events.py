import pygame
from constant import ARROWS
from load_game import get_grid



def check_events():
    
    grid = get_grid()
    if grid == None: return

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            
            if event.key in ARROWS:
                grid.make_move[event.key]()