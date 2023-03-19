import pygame

from constants import BLACK, MARRON, WHITE, LIGHT_YELLOW
from UI import font

pygame.init()

class ROW:

    Y = 0
    @classmethod
    def set_y(cls, v):
        cls.Y = v

    @classmethod
    def get_y(cls):
        return cls.Y

    max_width = 0
    @classmethod
    def get_w(cls):
        return cls.max_width

    @classmethod
    def set_w(cls, v):
        cls.max_width = v

    def __init__(self, texts, x_coord, y, on_click, font_size=40):

        self.font = font(font_size)
        self.texts = texts
        self.x_coord = x_coord
        self.y = y
        self.h = self.font.render('b', True, BLACK).get_rect().h
        self.on_click = on_click

    def render(self, color: tuple=WHITE):

        for t, x in zip(self.texts, self.x_coord):
            label = self.font.render(t, True, color)
            rct = label.get_rect()
            rct.topleft = (x, self.y)
            yield label, rct

    def draw(self, screen):

        rect = pygame.draw.rect(
            screen, LIGHT_YELLOW, 
            pygame.Rect(25, self.y - 5, 550, self.h + 10)
        )

        pos = pygame.mouse.get_pos()

        if rect.collidepoint(pos):

            pygame.draw.rect(
                screen, MARRON, rect
            )
            for l, r in self.render():
                screen.blit(l, r.topleft)

            if pygame.mouse.get_pressed()[0]:
                self.on_click()
        else:
            for l, r in self.render(BLACK):
                screen.blit(l, r.topleft)
