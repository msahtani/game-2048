from window import Window
from .widget import button
from constants import BLACK

from . import font, center
from constants import *
from game.game_state import GameState

from UI.grid import Grid2048
import pygame


class DoubleGrid(Grid2048):

    def __init__(self):
        self.screen  = pygame.display.set_mode((1150,600))
        self.grid = GameState.get()
        self.init_timer = pygame.time.get_ticks()

    def try_again(self):
        GameState.load(k=2)
        Window.switch(DoubleGrid)

    def draw(self):

        g1, g2 = self.grid[-1]

        self.screen.fill(
            LIGHT_YELLOW
        )
        
        # undo btn
        button.Button(60, 10,'UNDO', GameState.undo, font_size=25, eq_w=False) \
            .draw(self.screen)

        button.Button(0, 10, 'TRY AGAIN', self.try_again, font_size=25, beside=True, eq_w=False) \
            .draw(self.screen)

        button.Button(0, 10, 'EXIT', Window.switch, font_size=25, beside=True, eq_w=False) \
            .draw(self.screen)

        # timer
        timer_txt = font(23).render(self.timer(), True, BLACK)
        self.screen.blit(timer_txt, (button.Button.get_x() + 10, 10))

        #score
        score_txt = font(23).render('SCORE: %d' % (g1.score +  g2.score), True, BLACK)
        self.screen.blit(score_txt, (50, 50))

        #best score
        best_score_txt = font(23).render('BEST SCORE: %d' % g1.best_score, True, BLACK)
        self.screen.blit(best_score_txt, (250, 50))

        pygame.draw.rect(
            self.screen,
            LIGHT_MARRON,
            pygame.Rect(50, self.GRID_POS_Y, 500, 500),
            border_radius= 10
        )
        pygame.draw.rect(
            self.screen,
            LIGHT_MARRON,
            pygame.Rect(600, self.GRID_POS_Y, 500, 500),
            border_radius= 10
        )

        it = iter(g1)
        for i in range(16):
            n = next(it)
            r1 = pygame.draw.rect(
                self.screen, GRID_COLORS.get(n) or BLACK,
                pygame.Rect(55 + 125*(i%4), self.GRID_POS_Y + 5 + 125*(i//4), 115, 115),
                border_radius= 10
            )
            if n != 0:
                f= font()
                f.set_bold(True)
                text = f.render(str(int(n)), True, BLACK if n <= 2048 else WHITE)
                self.screen.blit(text, center(r1, text))

        it = iter(g2)
        for i in range(16):
            n = next(it)
            r2 = pygame.draw.rect(
                self.screen, GRID_COLORS.get(n) or BLACK,
                pygame.Rect(605 + 125*(i%4), self.GRID_POS_Y + 5 + 125*(i//4), 115, 115),
                border_radius= 10
            )
            if n != 0:
                f= font()
                f.set_bold(True)
                text = f.render(str(int(n)), True, BLACK if n <= 2048 else WHITE)
                self.screen.blit(text, center(r2, text))