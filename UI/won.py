from game.game_state import GameState
from window import Window
from .widget.button import Button
from . import center, font
from constants import *

class Won:

    def __init__(self):
        self.screen  = pygame.display.set_mode((600,600))

    def switch_to_game(self):
        grid = GameState.get()
        if len(grid[-1]) == 1:
            from .grid import Grid2048
            Window.switch(Grid2048)
        else:
            from .double_grid import DoubleGrid
            Window.switch(DoubleGrid)
    

    def draw(self):
        
        self.screen.fill(
            LIGHT_YELLOW
        )

        game_over_txt = font(75).render('YOU WON', True, BLACK)
        self.screen.blit(
            game_over_txt, 
            center(pygame.Rect(0,0,600,200), game_over_txt)
        )

        Button(None, 200, 'CONTINUE', self.switch_to_game)\
            .draw(self.screen)
        Button(None, 270, 'HOME', Window.switch)\
            .draw(self.screen)
            