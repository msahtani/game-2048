from game.game_state import GameState
from window import Window
from .widget.button import Button
from . import center, font
from constants import *

class GameOver:

    def __init__(self):
        self.screen  = pygame.display.set_mode((600,600))

    def switch_to_game(self):
        grid = GameState.get()
        if len(grid[-1]) == 1:
            from .grid import Grid2048
            GameState.load()
            Window.switch(Grid2048)
        else:
            from .double_grid import DoubleGrid
            GameState.load(k=2)
            Window.switch(DoubleGrid)
    
    def switch_to_home(self):        
        Window.switch()


    def draw(self):
        
        self.screen.fill(
            LIGHT_YELLOW
        )

        #game over
        
        game_over_txt = font(75).render('GAME OVER', True, BLACK)
        self.screen.blit(
            game_over_txt, 
            center(pygame.Rect(0,0,600,200), game_over_txt)
        )

        Button(None, 200, 'TRY AGAIN', self.switch_to_game)\
            .draw(self.screen)
        Button(None, 270, 'HOME', self.switch_to_home)\
            .draw(self.screen)
            