from model.rodillo import Rodillo


class Scene:
    def __init__(self):
        self.context = None  # el fondo del juego, podria ser un sprite, o una textura.
        self.rodillo = Rodillo()

    def draw(self):
        self.rodillo.draw()

    def rot_left(self):
        self.rodillo.rot_left()

    def rot_right(self):
        self.rodillo.rot_right()
