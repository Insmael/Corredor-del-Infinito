from random import random

from OpenGL.GL import *


class BlockStyle:
    def __init__(self):
        self.vertices = []
        self.vertices.append([])
        self.vertices.append([])
        self.vertices_default()
        self.color1 = self.rand_color()
        self.color2 = self.rand_color()
        self.z_pos = -100.0
        self.speed = 0.05
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.rot_ang = 0.0

    def rand_color(self):
        R = random()
        G = random()
        B = random()
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

    def set_pos(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos += z

    def set_rot_ang(self, rot_ang):
        self.rot_ang = rot_ang

    def draw(self, rot: float):
        glLoadIdentity()
        glRotatef(rot, 0.0, 0.0, 1.0)
        glTranslatef(self.x_pos, self.y_pos, self.z_pos)
        glRotatef(self.rot_ang, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)

        glColor3fv(self.color1)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][3])

        glColor3fv(self.color2)
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

        self.z_pos += self.speed
