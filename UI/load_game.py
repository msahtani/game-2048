from db.database import DBConnection
from game.game_state import GameState
from window import Window
from .widget.list_btn import ROW
import pygame
from .widget.button import Button
from constants import BLACK, LIGHT_YELLOW
from . import font

class LoadGame:

    pygame.KSCAN_X

    def __init__(self):
        self.screen  = pygame.display.set_mode((600,600))

        db = DBConnection()
        self.records = db.get_saved()
        db.close()

    def switch_to_game(self, id):
        from .grid import Grid2048
        GameState.load(id)
        Window.switch(Grid2048)

    def draw(self):
        
        self.screen.fill(
            LIGHT_YELLOW
        )

        HEADER = {
            'DATE': 30,
            'SCORE': 220,
            'LARGEST TILE': 350
        }
        for k, v in HEADER.items():
            label = font().render(k, True, BLACK)
            self.screen.blit(label, (v, 20))

        i = 0
        for row in self.records:
            # id, score, largest_tile, saved_at
            id, score, largest_tile, saved_at = row
            saved_at = str(saved_at)[:16]
            ROW((str(saved_at), str(score), str(largest_tile)),
                HEADER.values(), 50*(i+2), 
                lambda: self.switch_to_game(id), font_size=20
            ).draw(self.screen)
            i+= 1

        Button(None, 500, 'HOME', Window.switch)\
            .draw(self.screen)

             