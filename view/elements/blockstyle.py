from random import gauss

from OpenGL.GL import *

from model.axis import Axis


class BlockStyle:
    def __init__(self):
        self.vertices = []
        self.vertices.append([])
        self.vertices.append([])
        self.vertices_default()
        self.color1 = self.rand_color()
        self.color2 = self.color_2()
        self.pos = [0.0, 0.0]
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.rot_ang = 0.0

    def set_color(self, colors):
        self.color1 = self.rand_gauss_color(colors)
        self.color_2()

    def get_center(self):
        return self.pos[Axis.X], self.pos[Axis.Y]

    def rand_gauss_color(self, colors):
        R = gauss(colors[0], 0.05)
        G = gauss(colors[1], 0.05)
        B = gauss(colors[2], 0.05)
        return R, G, B

    def rand_color(self):
        R = gauss(0.1, 0.1)
        G = gauss(0.6, 0.1)
        B = gauss(0.6, 0.1)
        return R, G, B

    def color_2(self):
        R, G, B = self.color1
        R -= 0.1
        G -= 0.1
        B -= 0.1
        return R, G, B

    def def_vertices(self, vertices):
        self.vertices = vertices

    def vertices_default(self):
        self.vertices[0].append((1.0, 0.25, -2.0))
        self.vertices[0].append((-1.0, 0.25, -2.0))
        self.vertices[0].append((-1.0, 0.25, 2.0))
        self.vertices[0].append((1.0, 0.25, 2.0))

        self.vertices[1].append((1.0, -0.25, -2.0))
        self.vertices[1].append((-1.0, -0.25, -2.0))
        self.vertices[1].append((-1.0, -0.25, 2.0))
        self.vertices[1].append((1.0, -0.25, 2.0))

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

        """"
        glColor3f(1.0, 1.0, 1.0)
        glVertex3fv(self.vertices[1][0])
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[1][3])

        glColor3f(1.0, 0.0, 0.0)
        

        glColor3f(1.0, 0.5, 0.0)
        glVertex3fv(self.vertices[1][0])
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][0])
        

        glColor3f(1.0, 0.0, 1.0)
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][1])
        """

        glEnd()

    def full_draw(self, rot: float, z_pos):
        glLoadIdentity()
        # glRotatef(rot, 0.0, 0.0, 1.0)
        glTranslatef(self.pos[Axis.X], self.pos[Axis.Y], z_pos)
        # glRotatef(self.rot_ang, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)

        # glColor3fv(self.color2)
        # glVertex3fv(self.vertices[0][0])
        # glVertex3fv(self.vertices[0][1])
        # glVertex3fv(self.vertices[0][2])
        # glVertex3fv(self.vertices[0][3])

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
