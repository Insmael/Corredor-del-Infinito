from random import randint, gauss

from model.interactions.efects import *
from view.elements.blockstyle import BlockStyle


class Block:
    def __init__(self):
        self.style = BlockStyle()
        self.effect = NullEffect()
        self.make_interactive()

    def interact(self):
        pass

    def make_interactive(self):
        x = max(0.5, gauss(0.5, 0.3))
        if x > 0.7:
            y = randint(0, 3)
            if y == 0:
                self.effect = SpeedUpEffect()
                self.style.set_color((0.9, 0.9, 0.1))
            if y == 1:
                self.effect = SpeedDownEffect()
                self.style.set_color((0.9, 0.1, 0.1))
            if y == 2:
                self.effect = LightChangeEffect()
                self.style.set_color((0.8, 0.8, 0.8))
            if y == 3:
                self.effect = PointEffect()
                self.style.set_color((0.1, 0.0, 0.9))

    def set_rot_ang(self, rot_ang):
        self.style.set_rot_ang(rot_ang)

    def set_pos(self, x, y):
        self.style.set_pos(x, y)

    def def_vertices(self, vertices):
        self.style.set_vertices(vertices)

    def draw(self, rot, z_pos):
        self.style.draw(rot, z_pos)

    def get_center(self):
        return self.style.get_center()

    def eff_to_str(self):
        return str(self.effect)

    def interact(self, rodillo):
        self.effect.interact(rodillo)
