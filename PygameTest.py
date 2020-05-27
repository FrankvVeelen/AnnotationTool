import pygame as pg
from main_menu import MainMenu
from states import *

pg.init()
size = 1000, 1000
screen = pg.display.set_mode(size, pg.SRCALPHA, 32)
pg.display.set_caption("Hyperion Annotation Tool (HAT)")
state = IN_MENU
menu = None
annotation_screen = None

done = False

while not done:
    mouse_pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            break
        elif state == IN_MENU and menu is not None:
            menu.handle_event(event)
    if state == IN_MENU:
        if menu is None:
            menu = MainMenu(screen)
        else:
            menu.draw(mouse_pos)
    elif state == IN_LABEL_SIMPLE:
        if annotation_screen is None:
            annotation_screen =


    pg.display.update()