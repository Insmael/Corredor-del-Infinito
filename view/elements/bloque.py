from OpenGL.GL import *


class Bloque:
    def __init__(self):
        self.vertices = []
        self.vertices.append([])
        self.vertices.append([])
        self.vertices_default()

        self.z_pos = -100.0
        self.speed = 0.2
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.rot_ang = 0.0

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
        self.x_pos = x
        self.y_pos = y

    def set_rot_ang(self, rot_ang):
        self.rot_ang = rot_ang

    def draw(self):
        glLoadIdentity()
        glTranslatef(self.x_pos, self.y_pos, self.z_pos)
        glRotatef(self.rot_ang, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][3])

        glColor3f(1.0, 1.0, 1.0)
        glVertex3fv(self.vertices[1][0])
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[1][3])

        glColor3f(1.0, 0.0, 0.0)
        glVertex3fv(self.vertices[0][3])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[1][3])

        glColor3f(1.0, 0.5, 0.0)
        glVertex3fv(self.vertices[1][0])
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[0][1])
        glVertex3fv(self.vertices[0][0])

        glColor3f(0.0, 0.0, 1.0)
        glVertex3fv(self.vertices[0][0])
        glVertex3fv(self.vertices[0][3])
        glVertex3fv(self.vertices[1][3])
        glVertex3fv(self.vertices[1][0])

        glColor3f(1.0, 0.0, 1.0)
        glVertex3fv(self.vertices[1][1])
        glVertex3fv(self.vertices[1][2])
        glVertex3fv(self.vertices[0][2])
        glVertex3fv(self.vertices[0][1])
        glEnd()

        self.z_pos += self.speed
