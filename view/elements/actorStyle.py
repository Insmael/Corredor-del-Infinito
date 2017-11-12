from model.axis import Axis
from view.elements.blockstyle import BlockStyle


class Actor:
    pass


class RectangleActor(Actor):
    def __init__(self, pos=([0.0, -0.15, -0.7])):
        self.pos = pos
        self.widht = 0.07
        self.height = 0.10
        self.deep = 0.10
        self.rectangle = BlockStyle()
        self.rectangle.set_pos(self.pos[Axis.X], self.pos[Axis.Y])
        self.rectangle.def_vertices([[[self.widht / 2, -self.height / 2, self.deep / 2],
                                      [self.widht / 2, self.height / 2, self.deep / 2],
                                      [-self.widht / 2, self.height / 2, self.deep / 2],
                                      [-self.widht / 2, -self.height / 2, self.deep / 2]],
                                     [[self.widht / 2, -self.height / 2, -self.deep / 2],
                                      [self.widht / 2, self.height / 2, -self.deep / 2],
                                      [-self.widht / 2, self.height / 2, -self.deep / 2],
                                      [-self.widht / 2, -self.height / 2, -self.deep / 2]]])
        self.rectangle.set_color((1.4, 1.4, 1.4))

    def draw(self, rot: float):
        self.rectangle.full_draw(rot, self.pos[Axis.Z])
