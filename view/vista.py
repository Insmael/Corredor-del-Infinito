# from controler.game_driver import GameDriver
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from view.scene import MenuScene, Scene
from view.screen_sizes import Resolution


class Vista:

    def __init__(self):
        self.prepare()
        self.game_scene = Scene()
        self.menu_scene = MenuScene()
        self.actual_scene = self.menu_scene

    def resize(self, resolution):
        width = resolution[0]
        height = resolution[1]
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
        video_flags = OPENGL | DOUBLEBUF | RESIZABLE
        pygame.init()
        pygame.display.set_mode(Resolution.LARGE.value, video_flags)
        self.resize(Resolution.LARGE.value)
        self.init()

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_all()
        pygame.display.flip()

    def draw_all(self):
        self.actual_scene.draw()

    def jump_left(self):
        self.game_scene.jump_left()

    def jump_right(self):
        self.game_scene.jump_right()

    def jump_straight(self):
        self.game_scene.jump_straight()

    def fall(self):
        self.game_scene.fall()
