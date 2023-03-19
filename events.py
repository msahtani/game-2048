import pygame
from copy import deepcopy
from game.game_state import GameState
from constants import ARROWS
from game.game_logic import Game2048
from window import Window


def check_event():

    grid: list[Game2048] = GameState.get()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if not grid: return
        
        elif event.type == pygame.KEYDOWN:
            if event.key in ARROWS:
                grid += [deepcopy(grid[-1])]
                for g in grid[-1]:
                    g.make_move(event.key)

                    if g.game_over:
                        from UI.game_over import GameOver
                        Window.switch(GameOver)
                    
                    elif g.won:
                        from UI.won import Won
                        Window.switch(Won)

                if len(grid) > 10:
                    grid.pop(0)
            
            elif event.key == pygame.K_s:
                grid[-1][0].save()

            elif event.key == pygame.K_u:
                GameState.undo()

            elif event.key == pygame.K_q:
                grid[-1][0].save()
                quit()
   