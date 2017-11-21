from math import cos
from random import gauss

from OpenGL.GL import *

from model.axis import Axis


class BlockStyle:
    def __init__(self):
        self.vertices = []
        self.color1 = self.rand_gauss_color((0.1, 0.6, 0.6), 1.0)
        self.color2 = self.color_2()
        self.pos = [0.0, 0.0]
        self.rot_ang = 0.0

    def set_color(self, colors, alfa=1.0):
        self.color1 = self.rand_gauss_color(colors, alfa)
        self.color_2()

    def get_center(self):
        return self.pos[Axis.X], self.pos[Axis.Y]

    def rand_gauss_color(self, colors, alfa=1.0):
        r = gauss(colors[0], 0.05)
        g = gauss(colors[1], 0.05)
        b = gauss(colors[2], 0.05)
        return r, g, b, alfa

    def color_2(self):
        r, g, b, a = self.color1
        return r - 0.1, g - 0.1, b - 0.1, a

    def set_vertices(self, vertices):
        self.vertices = vertices

    def set_pos(self, x, y):
        self.pos[Axis.X] = x
        self.pos[Axis.Y] = y

    def set_rot_ang(self, rot_ang):
        self.rot_ang = rot_ang

    def draw(self, rot: float, z_pos):

        glLoadIdentity()
        glRotatef(rot, 0.0, 0.0, 1.0)
        glTranslatef(self.pos[Axis.X], self.pos[Axis.Y], z_pos)
        glRotatef(self.rot_ang, 0.0, 0.0, 1.0)

        glBegin(GL_QUADS)
        glColor4fv(self.color2)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][3])
        glColor4fv(self.color1)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][3])
        glVertex3fv(self.vertices[1][3])
        glVertex3fv(self.vertices[1][0])
        glEnd()

    def full_draw(self, pos, ang=0.0):
        glLoadIdentity()
        glTranslatef(pos[Axis.X], pos[Axis.Y], pos[Axis.Z])
        if ang:
            dy = -abs(self.vertices[0][2][1] - self.vertices[0][3][1])
            glTranslatef(0.0, -dy * abs(cos(ang)) * 0.2, dy * cos(ang) * 0.9)
            glRotatef(90 * cos(ang), 1.0, 0.0, 0.0)
        glBegin(GL_QUADS)

        glColor4fv(self.color1)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][3])

        glColor4fv(self.color2)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][3])
        glVertex3fv(self.vertices[1][3])
        glVertex3fv(self.vertices[1][0])

        glVertex3fv(self.vertices[1][0])
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[1][3])

        glVertex3fv(self.vertices[1][0])
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][0])

        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][1])
        glEnd()
