from OpenGL.GL import *

from view.elements.bloque import Bloque


class Scene:
    def __init__(self):
        self.context = None
        self.figures = []
        self.fig1 = Bloque()
        self.fig2 = Bloque()
        self.fig3 = Bloque()
        self.fig4 = Bloque()

        self.fig1.set_pos(0.0, -4.0)
        self.fig2.set_pos(0.0, 4.0)
        self.fig3.set_pos(4.0, 0.0)
        self.fig4.set_pos(-4.0, 0.0)

        self.fig2.set_rot_ang(180)
        self.fig3.set_rot_ang(90)
        self.fig4.set_rot_ang(-90)

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

        self.fig1.draw()
        self.fig2.draw()
        self.fig3.draw()
        self.fig4.draw()
