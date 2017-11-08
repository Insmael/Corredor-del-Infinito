# from controler.game_driver import GameDriver
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from view.scene import Scene


class Vista:
    # def update(self, game_driver: GameDriver):
    """
    dibuja los elementos que necesitan ser nuevamente dibujados en la nueva escena.
    :param game_driver: la instancia del juego completo que se busca dibujar
    :return:
    """

    #   list_of_changes = game_driver.get_changed()
    #   self.draw(list_of_changes)

    # def draw(self, list_of_changes):


    def __init__(self):

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

    def draw_all(self):
        self.scene.draw()

    def run_me(self):
        video_flags = OPENGL | DOUBLEBUF

        pygame.init()
        pygame.display.set_mode((640, 480), video_flags)

        self.resize(640, 480)
        self.init()

        frames = 0
        ticks = pygame.time.get_ticks()
        while 1:
            event = pygame.event.poll()
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                break

            self.draw_all()
            pygame.display.flip()
            frames = frames + 1
