from window import Window
from .widget import button

from . import font, center
from constants import *
from game.game_state import GameState

class Grid2048:
    
    GRID_POS_Y = 90

    def __init__(self):
        self.grid = GameState.get()
        self.screen  = pygame.display.set_mode((600,600))
        self.init_timer = pygame.time.get_ticks()


    def timer(self):
        sec = (pygame.time.get_ticks() - self.init_timer ) // 1000
        sec, min = sec % 60, sec // 60
        
        sec = ('0' if sec < 10 else '') + str(sec) 
        min = ('0' if min < 10 else '') + str(min)

        return min+':'+sec


    def try_again(self):
        GameState.load()
        Window.switch(Grid2048)
        

    def draw(self):
        grid, = self.grid[-1]

        self.screen.fill(
            LIGHT_YELLOW
        )
        pygame.draw.rect(
            self.screen,
            LIGHT_MARRON,
            pygame.Rect(50, self.GRID_POS_Y, 500, 500),
            border_radius=10
        )

        # undo btn
        button.Button(60, 10,'UNDO', GameState.undo, font_size=25, eq_w=False) \
            .draw(self.screen)

        # save btn
        button.Button(0, 10, 'SAVE', self.grid[-1][0].save, font_size=25, beside=True, eq_w=False) \
            .draw(self.screen)

        button.Button(0, 10, 'TRY AGAIN', self.try_again, font_size=25, beside=True, eq_w=False) \
            .draw(self.screen)

        button.Button(0, 10, 'EXIT', Window.switch, font_size=25, beside=True, eq_w=False) \
            .draw(self.screen)

        # timer
        timer_txt = font().render(self.timer(), True, BLACK)
        self.screen.blit(timer_txt, (button.Button.get_x() + 10, 10))

        #score
        score_txt = font(23).render('SCORE: %d' % grid.score, True, BLACK)
        self.screen.blit(score_txt, (50, 50))

        #best score
        best_score_txt = font(23).render('BEST SCORE: %d' % grid.best_score, True, BLACK)
        self.screen.blit(best_score_txt, (250, 50))
        
        it = iter(grid)
        for i in range(4*4):
            n = next(it)
            r = pygame.draw.rect(
                self.screen, GRID_COLORS.get(n) or BLACK,
                pygame.Rect(55 + 125*(i%4), self.GRID_POS_Y + 5 + 125*(i//4), 115, 115),
                border_radius= 10
            )
            if n != 0:
                f = font()
                f.set_bold(True)
                text = f.render(str(int(n)), True, BLACK if n <= 2048 else WHITE)
                self.screen.blit(text, center(r, text))