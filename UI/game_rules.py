import pygame

from window import Window
from . import font, center
from constants import *
from .widget.button import Button

class GameRules:

    def __init__(self):
        self.screen  = pygame.display.set_mode((600,600))
        self.rules = [
            '       swipe the screen up, down ,right or left to move all',
            ' numbers tiles in that diredtion. Each tile moves in that',
            'direction until it the wall or another tile hits the wall',
            'or another tile (use your arrow keys in the computer vision)',
            '',
            '       each time you make a move, a new 2 or 4 tile appears in',
            'empoty spot in a row or column that was moved last move'
        ]

    
    def draw(self):
        self.screen.fill(
            LIGHT_YELLOW
        )
        f = font(30)
        f.set_bold(True)
        title = f.render('GAME RULES', True, (0,0,0))
        self.screen.blit(title, center(pygame.Rect(0,0,600,150), title))

        i = 150
        for l in self.rules:
            if len(l) != 0:
                text = font(20).render(l, True, (0,0,0))
                self.screen.blit(text, (20, i))
            i+= 20

        Button(None, 500, 'HOME', Window.switch)\
            .draw(self.screen)