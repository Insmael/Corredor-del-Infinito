from random import gauss

from OpenGL.GL import *

from model.axis import Axis


class BlockStyle:
    def __init__(self):
        self.vertices = []
        self.color1 = self.rand_gauss_color((0.1, 0.6, 0.6))
        self.color2 = self.color_2()
        self.pos = [0.0, 0.0]
        self.rot_ang = 0.0

    def set_color(self, colors):
        self.color1 = self.rand_gauss_color(colors)
        self.color_2()

    def get_center(self):
        return self.pos[Axis.X], self.pos[Axis.Y]

    def rand_gauss_color(self, colors):
        r = gauss(colors[0], 0.05)
        g = gauss(colors[1], 0.05)
        b = gauss(colors[2], 0.05)
        return r, g, b

    def color_2(self):
        r, g, b = self.color1
        return r - 0.1, g - 0.1, b - 0.1

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
        glColor3fv(self.color2)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][3])
        glColor3fv(self.color1)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][3])
        glVertex3fv(self.vertices[1][3])
        glVertex3fv(self.vertices[1][0])
        glEnd()

    def full_draw(self, pos):
        glLoadIdentity()
        glTranslatef(pos[Axis.X], pos[Axis.Y], pos[Axis.Z])
        glBegin(GL_QUADS)
        """
        glColor3fv(self.color2)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][3])
        """
        glColor3fv(self.color1)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][3])
        glVertex3fv(self.vertices[1][3])
        glVertex3fv(self.vertices[1][0])

        # glVertex3fv(self.vertices[1][0])
        # glVertex3fv(self.vertices[1][1])
        # glVertex3fv(self.vertices[1][2])
        # glVertex3fv(self.vertices[1][3])

        # glVertex3fv(self.vertices[1][0])
        # glVertex3fv(self.vertices[1][1])
        # glVertex3fv(self.vertices[0][1])
        # glVertex3fv(self.vertices[0][0])

        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][1])
        glEnd()
