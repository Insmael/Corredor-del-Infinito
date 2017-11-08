from OpenGL.GL import *

from view.elements.bloque import Bloque
from view.vertex_generator import Vertex_generator


class Scene:
    def __init__(self):
        self.context = None
        self.figures = []
        self.fig1 = Bloque()
        self.fig2 = Bloque()
        self.fig3 = Bloque()
        self.fig4 = Bloque()
        faces = 8
        self.vert_gen = Vertex_generator(1, faces, 0.2)

        centers_pos = self.vert_gen.centers_pos()
        rot_angs = self.vert_gen.rot_angs()
        all_vert = self.vert_gen.all_body_verteces(20)
        for i in range(faces):
            b = Bloque()
            b.set_rot_ang(rot_angs[i])
            b.set_pos(centers_pos[i][0], centers_pos[i][1])
            b.def_vertices(all_vert)
            self.figures.append(b)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        """
        glLoadIdentity()
        glTranslatef(-1.5, 0.0, -60.0)

        glRotatef(self.rtri, 0.0, 1.0, 0.0)

        glBegin(GL_TRIANGLES)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glEnd()

        """
        for fig in self.figures:
            fig.draw()
