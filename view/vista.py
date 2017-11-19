# from controler.game_driver import GameDriver
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from controler.event_manager import EventManager
from view.scenes import MainMenuScene, GameScene, GameOverScene, PauseScene
from view.screen_sizes import Resolution


class Vista:

    def __init__(self):
        self.prepare()
        self.event_manager = EventManager()
        self.game_scene = GameScene()
        self.menu_scene = MainMenuScene()
        self.pause_scene = PauseScene()
        self.game_over_scene = GameOverScene()
        self.actual_scene = self.menu_scene
        self.game_speed = 1.0
        self.game_block_ratio = 1.0

    def prepare(self):
        video_flags = OPENGL | DOUBLEBUF | RESIZABLE
        pygame.init()
        # resize window
        pygame.display.set_mode(Resolution.LARGE.value, video_flags)
        width = Resolution.LARGE.value[0]
        height = Resolution.LARGE.value[1]
        if height == 0:
            height = 1
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # init
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    def run(self):
        while True:
            self.event_manager.update(self)
            self.update()
            self.try_game_over()

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.actual_scene.draw()
        pygame.display.flip()

    def rot_left(self):
        self.game_scene.jump_left()

    def rot_right(self):
        self.game_scene.jump_right()

    def jump_straight(self):
        self.game_scene.jump_straight()

    def fall(self):
        self.game_scene.fall()

    def select_menu_item(self):
        self.actual_scene.select(self)

    def before_menu_item(self):
        self.actual_scene.before_item()

    def next_menu_item(self):
        self.actual_scene.next_item()

    def set_medium(self):
        self.game_speed = 2.0
        self.game_block_ratio = 0.5

    def set_easy(self):
        self.game_speed = 1.0
        self.game_block_ratio = 1.0

    def set_hard(self):
        self.game_speed = 4.0
        self.game_block_ratio = 0.2

    def start_game(self):
        self.game_scene.set_difficulty(self.game_speed, self.game_block_ratio)
        self.event_manager.in_menu = False
        self.actual_scene = self.game_scene
        self.update()
        pygame.time.delay(500)

    def set_pause(self):
        self.actual_scene = self.pause_scene
        self.event_manager.in_menu = True
        pygame.time.delay(500)

    def set_unpause(self):
        self.actual_scene = self.game_scene
        self.event_manager.in_menu = False
        self.update()
        pygame.time.delay(500)

    def set_main_menu(self):
        self.actual_scene = self.menu_scene
        self.menu_scene.reestart()
        self.game_scene.reestart()
        self.set_easy()
        self.pause_scene.reestart()

    def game_over(self):
        self.menu_scene.reestart()
        self.game_scene.reestart()
        self.pause_scene.reestart()

    def try_game_over(self):
        if self.game_scene.actor.is_game_over():
            self.actual_scene = self.game_over_scene
            self.event_manager.in_menu = True
