from GUI_SETTINGS import *

class AnnotationScreen:
    def __init__(self, screen):
        self.surface = screen.subsurface((0, 0), screen.get_size())  # take full screen for annotation screen
        self.img_surface = self.surface.subsurface((0, 0), IMAGE_SIZE)
        self.img_to_annotate = "images/car.jpg"

    def draw_image(self):
        pass