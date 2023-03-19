from UI import font
import pygame
from constants import BLACK, LIGHT_YELLOW, MARRON, WHITE, WIDTH

class Button:

    DELAY = 200
    max_width = 0
    last_x = 0

    @classmethod
    def get_x(cls):
        return cls.last_x

    @classmethod
    def set_x(cls, v):
        cls.last_x = v

    @classmethod
    def get_max_w(cls):
        return cls.max_width

    @classmethod
    def set_max_w(cls, v:float):
        cls.max_width = v

    def __init__(self, x, y, text: str, on_click, font_size=40, eq_w = True, beside = False):
        # eq w
        self.eqw = eq_w

        # setup font
        self.font = font(font_size)
        self.font.get_bold()
        
        self.text = text
        # get rect
        self.rect = self.render_text().get_rect()
        
        if self.rect.w + 20 >= Button.get_max_w():
            Button.set_max_w(self.rect.w + 20)

        if x == None:
            x = (WIDTH - self.rect.width) / 2
        elif beside:
            x = Button.get_x()
        
        self.rect.topleft = (x, y)
        self.on_click = on_click

        Button.set_x(self.rect.bottomright[0] + 15)

    def render_text(self, color = BLACK):
        return self.font.render(self.text, True, color)

    def draw(self, screen):
        # get mouse position
        pos = pygame.mouse.get_pos()

        text = None

        #check mouse over and click conditions
        if self.eqw:
            W, X = self.max_width, self.rect.center[0] - self.max_width/2
        else:
            W, X = self.rect.w + 10, self.rect.x - 5


        if self.rect.collidepoint(pos):
            pygame.draw.rect(
                screen, LIGHT_YELLOW, 
                pygame.Rect(X, self.rect.y - 5, W, self.rect.h + 10),
                border_radius=5,
                
            )
            text = self.render_text(BLACK)
            if pygame.mouse.get_pressed()[0] == 1:
                if self.on_click:
                    self.on_click()
                pygame.time.delay(self.DELAY)
        else:
            pygame.draw.rect(
                screen, MARRON, 
                pygame.Rect(X, self.rect.y - 5, W, self.rect.h + 10),
                border_radius=5
            )
            text = self.render_text(WHITE)

        # draw button on screen
        screen.blit(text, self.rect.topleft)