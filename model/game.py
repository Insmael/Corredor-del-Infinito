from model.actor import Actor
from model.mapa import Mapa
from model.objetos import Objetos


class Game:
    def __init__(self):
        self.map = Mapa()
        self.actor = Actor()
        self.objetos = Objetos()

    def jump_straight(self):
        self.actor.jumping()

    def jump_right(self):
        self.map.rotar_der()
        self.actor.jumping()

    def jump_left(self):
        self.map.rotar_izq()
        self.actor.jumping()

    def fall(self):
        self.actor.stop_jumping()
