from math import sin, pi, exp

from pygame.time import get_ticks

from model.axis import Axis
from view.elements.blockstyle import BlockStyle


class Actor:
    def __init__(self, pos=([0.0, -0.15, -0.7])):
        self.pos = pos
        self.widht = 0.07
        self.height = 0.10
        self.deep = 0.10
        self.rectangle = BlockStyle()
        self.rectangle.set_pos(self.pos[Axis.X], self.pos[Axis.Y])
        self.rectangle.set_vertices(self.get_vertices(self.widht, self.height, self.deep))
        self.rectangle.set_color((1.4, 1.4, 1.4))
        self.jumping = False
        self.falling = False
        self.delta_jump_frame = 0.0105
        self.jump_limit = 0.035
        self.jump_floor = -0.15
        self.jump_ang = 0.0
        self.jump_ratio = 1.0

    def get_vertices(self, widht, height, deep):
        return [[[widht / 2, -height / 2, deep / 2],
                 [widht / 2, height / 2, deep / 2],
                 [-widht / 2, height / 2, deep / 2],
                 [-widht / 2, -height / 2, deep / 2]],
                [[widht / 2, -height / 2, -deep / 2],
                 [widht / 2, height / 2, -deep / 2],
                 [-widht / 2, height / 2, -deep / 2],
                 [-widht / 2, -height / 2, -deep / 2]]]

    def draw(self, speed):
        if self.falling:
            self.jump_ang -= self.delta_jump_frame * 4
            self.pos[Axis.Y] = self.jump_floor + sin(self.jump_ang) * (
            self.jump_limit - self.jump_floor) * self.jump_ratio
        if self.jumping:
            self.jump_ang += self.delta_jump_frame
            self.pos[Axis.Y] = self.jump_floor + sin(self.jump_ang) * (
            self.jump_limit - self.jump_floor) * self.jump_ratio
        if self.pos[Axis.Y] >= self.jump_limit - 0.001:
            self.jumping = False
            self.falling = True
        self.draw_figure(speed)

    def draw_figure(self, speed):
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

    def is_standing(self):
        return not self.falling and not self.jumping

    def moving(self):
        return self.is_falling() or self.is_jumping()

    def normal_fall(self):
        if not self.jumping:
            self.falling = True

    def is_game_over(self):
        return self.pos[Axis.Y] < self.jump_floor - 0.15


class ActorHomoMorfo(Actor):
    def __init__(self, pos=([0.0, -0.15, -0.7])):
        super(ActorHomoMorfo, self).__init__(pos)
        self.body = BlockStyle()
        self.leg1 = BlockStyle()
        self.leg2 = BlockStyle()
        self.hips = BlockStyle()
        self.neck = BlockStyle()
        self.head = BlockStyle()
        self.arm1 = BlockStyle()
        self.arm2 = BlockStyle()
        self.arrange_full_body()

    def head_pos(self):
        return self.relative_pos((0.0, 0.07, 0.0))

    def body_pos(self):
        return self.relative_pos((0.0, 0.04, 0.0))

    def leg1_pos(self):
        return self.relative_pos((0.01, 0.0, 0.0))

    def leg2_pos(self):
        return self.relative_pos((-0.01, 0.0, 0.0))

    def hips_pos(self):
        return self.relative_pos((0.0, 0.02, 0.0))

    def neck_pos(self):
        return self.relative_pos((0.0, 0.05, 0.0))

    def arm1_pos(self):
        return self.relative_pos((0.025, 0.035, 0.0))

    def arm2_pos(self):
        return self.relative_pos((-0.025, 0.035, 0.0))

    def relative_pos(self, deltas):
        return self.pos[Axis.X] + deltas[Axis.X], self.pos[Axis.Y] + deltas[Axis.Y], self.pos[Axis.Z] + deltas[Axis.Z]

    def arrange_full_body(self):
        self.body.set_vertices(self.get_vertices(self.widht / 2, self.height / 4, self.deep / 8))
        self.body.set_color((1.0, 0.1, 0.2), 1.0)

        self.head.set_vertices(self.get_vertices(self.widht / 2, self.height / 3.5, self.deep / 7))
        self.head.set_color((1.0, 0.1, 0.2), 1.5)

        self.leg1.set_vertices(self.get_vertices(self.widht / 5, self.height / 3.5, self.deep / 10))
        self.leg1.set_color((1.0, 0.1, 0.2), 1.5)

        self.leg2.set_vertices(self.get_vertices(self.widht / 5, self.height / 3.5, self.deep / 10))
        self.leg2.set_color((1.0, 0.1, 0.2), 1.5)

        self.hips.set_vertices(self.get_vertices(self.widht / 2, self.height / 5, self.deep / 8))
        self.hips.set_color((1.0, 0.1, 0.2), 0.5)

        self.neck.set_vertices(self.get_vertices(self.widht / 3, self.height / 3.5, self.deep / 9))
        self.neck.set_color((1.0, 0.1, 0.2), 0.5)

        self.arm1.set_vertices(self.get_vertices(self.widht / 5.2, self.height / 3.5, self.deep / 10))
        self.arm1.set_color((1.0, 0.1, 0.2), 0.5)

        self.arm2.set_vertices(self.get_vertices(self.widht / 5.2, self.height / 3.5, self.deep / 10))
        self.arm2.set_color((1.0, 0.1, 0.2), 0.5)

    def draw_figure(self, speed):
        # self.rectangle.full_draw(self.pos)
        max_speed = 100
        c = max_speed * (1 - exp(-speed / 5))
        self.body.full_draw(self.body_pos())
        self.head.full_draw(self.head_pos())
        self.leg1.full_draw(self.leg1_pos(), pi + c * get_ticks() / 500)
        self.leg2.full_draw(self.leg2_pos(), c * get_ticks() / 500)
        self.hips.full_draw(self.hips_pos())
        self.neck.full_draw(self.neck_pos())
        self.arm1.full_draw(self.arm1_pos(), c * get_ticks() / 500)
        self.arm2.full_draw(self.arm2_pos(), pi + c * get_ticks() / 500)
