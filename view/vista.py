# from controler.game_driver import GameDriver
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from view.scene import Scene


class Vista:

    def __init__(self):
        self.prepare()
        self.scene = Scene()

    def resize(self, width, height):
        if height == 0:
            height = 1
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def init(self):
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    def prepare(self):
        video_flags = OPENGL | DOUBLEBUF
        pygame.init()
        pygame.display.set_mode((640, 480), video_flags)
        self.resize(640, 480)
        self.init()

    def update(self):
        self.draw_all()
        pygame.display.flip()

    def draw_all(self):
        self.scene.draw()

    def rot_left(self):
        self.scene.rot_left()

    def rot_right(self):
        self.scene.rot_right()
