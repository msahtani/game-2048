from UI import center
from game.game_state import GameState
from window import Window
from .widget import button
from constants import *

class Home:
    
    def __init__(self):
        self.screen  = pygame.display.set_mode((600,600))

    def switch_to_game(self):
        from UI.grid import Grid2048
        GameState.load()
        Window.switch(Grid2048)

    def switch_to_load(self):
        from .load_game import LoadGame
        Window.switch(LoadGame)

    def switch_to_opt(self):
        from .ng_option import NewGameOpt
        Window.switch(NewGameOpt)

    def switch_to_game_rules(self):
        from .game_rules import GameRules
        Window.switch(GameRules)

    def draw(self):
        self.screen.fill(LIGHT_YELLOW)

        image = pygame.image.load('./assets/logo.png')
        image = pygame.transform.scale(image, (200,200))
        self.screen.blit(image, center(pygame.Rect(0,25,600,200), image))

        button.Button(None, 250, 'NEW GAME', self.switch_to_opt)\
            .draw(self.screen)
        button.Button(None, 320, 'LOAD GAME', self.switch_to_load)\
            .draw(self.screen)
        button.Button(None, 390, 'GAME RULES', self.switch_to_game_rules)\
            .draw(self.screen)
        button.Button(None, 460, 'QUIT', exit)\
            .draw(self.screen)