import pygame

pygame.init()
font = lambda x=30: pygame.font.SysFont('arial', x)

def center(r: pygame.Rect, text):
    t = text.get_rect()
    return (r.x + (r.width - t.width)/2, r.y + (r.height - t.height)/2)    


def hex_to_rgb(string):
    return int(string[1:3], 16), int(string[3:5], 16), int(string[5:], 16)