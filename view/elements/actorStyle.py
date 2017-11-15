from math import sin

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
        self.rectangle.set_vertices([[[self.widht / 2, -self.height / 2, self.deep / 2],
                                      [self.widht / 2, self.height / 2, self.deep / 2],
                                      [-self.widht / 2, self.height / 2, self.deep / 2],
                                      [-self.widht / 2, -self.height / 2, self.deep / 2]],
                                     [[self.widht / 2, -self.height / 2, -self.deep / 2],
                                      [self.widht / 2, self.height / 2, -self.deep / 2],
                                      [-self.widht / 2, self.height / 2, -self.deep / 2],
                                      [-self.widht / 2, -self.height / 2, -self.deep / 2]]])
        self.rectangle.set_color((1.4, 1.4, 1.4))
        self.jumping = False
        self.falling = False
        self.delta_jump_frame = 0.01
        self.jump_limit = 0.05
        self.jump_floor = -0.15
        self.jump_ang = 0.0

    def draw(self):
        if self.falling:
            self.jump_ang -= self.delta_jump_frame * 2
            self.pos[Axis.Y] = self.jump_floor + sin(self.jump_ang) * (self.jump_limit - self.jump_floor)
        if self.jumping:
            self.jump_ang += self.delta_jump_frame
            self.pos[Axis.Y] = self.jump_floor + sin(self.jump_ang) * (self.jump_limit - self.jump_floor)
        if self.pos[Axis.Y] >= self.jump_limit - 0.001:
            self.jumping = False
            self.falling = True
        self.rectangle.full_draw(self.pos)

    def set_jumping(self, can_jump):
        if can_jump:
            self.jumping = True
            self.pos[Axis.Y] += self.delta_jump_frame * 2

    def fall(self):
        if self.jumping:
            self.jumping = False
            self.falling = True

    def stop_falling(self):
        if self.falling and -0.20 < self.pos[Axis.Y] <= -0.15:
            self.falling = False
        if abs(self.pos[Axis.Y] + 0.15) <= 0.005:
            self.pos[Axis.Y] = self.jump_floor

    def is_jumping(self):
        return self.jumping

    def is_falling(self):
        return self.falling

    def moving(self):
        return self.is_falling() or self.is_jumping()

    def normal_fall(self):
        if not self.jumping:
            self.falling = True
