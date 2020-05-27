import pygame as pg
from text_input import TextInput

class MainMenu:
    def __init__(self, screen):
        self.surface = screen.subsurface((0,0), screen.get_size())  # take full screen for menu
        self.name_input = TextInput()

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONUP:
            self.handle_click(event.pos)
        else:
            self.name_input.update([event])

    def handle_click(self, position):
        pass

    def draw(self, mouse_pos):
        self.surface.fill((225, 225, 225))
        self.surface.blit(self.name_input.get_surface(), (10, 10))