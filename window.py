import pygame

class Window:

    ui = None # type or obj

    @classmethod
    def switch(cls, ui = None):
        if ui == None:
            from UI.home import Home
            cls.ui = Home
        else:
            cls.ui = ui

    @classmethod
    def draw_window(cls):
        
        if type(cls.ui) == type:
            cls.ui = cls.ui()
        else:
            cls.ui.draw()

        pygame.display.update()
