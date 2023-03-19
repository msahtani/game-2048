from game.game_state import GameState
from window import Window
from .widget.button import Button

from constants import *

class NewGameOpt:

    def __init__(self):
        self.screen  = pygame.display.set_mode((600,600))

    def switch_to_grid(self):
        from .grid import Grid2048
        GameState.load()
        Window.switch(Grid2048)

    def switch_to_double_grid(self):
        from .double_grid import DoubleGrid
        GameState.load(k=2)
        Window.switch(DoubleGrid)
    
    def switch_to_home(self):        
        Window.switch()


    def draw(self):
        
        self.screen.fill(
            LIGHT_YELLOW
        )

        Button(None, 100, 'NORMAL', self.switch_to_grid)\
            .draw(self.screen)
        Button(None, 200, 'DOUBLE', self.switch_to_double_grid)\
            .draw(self.screen)
        Button(None, 500, 'HOME', self.switch_to_home)\
            .draw(self.screen)
            