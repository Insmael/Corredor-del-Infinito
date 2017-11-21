import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from model import soundengine
from model.event_manager import EventManager
from view.lightengine import LightEnginne
from view.scenes import MainMenuScene, GameScene, GameOverScene, PauseScene


class GameEngine:
    def __init__(self, screen_size):
        self.prepare(screen_size)
        self.event_manager = EventManager()
        self.game_scene = GameScene()
        self.menu_scene = MainMenuScene()
        self.pause_scene = PauseScene()
        self.game_over_scene = GameOverScene()
        self.light_engine = LightEnginne()
        self.actual_scene = self.menu_scene
        self.game_speed = 1.0
        self.game_block_ratio = 1.0
        self.jump_ratio = 1.0
        soundengine.play_main_song()

    def in_menu(self):
        return self.actual_scene != self.game_scene

    def prepare(self, screen_size):
        video_flags = OPENGL | DOUBLEBUF | RESIZABLE
        pygame.init()
        # resize window
        pygame.display.set_mode(screen_size, video_flags)
        width = screen_size[0]
        height = screen_size[1]
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
        glEnable(GL_LIGHTING)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_COLOR_MATERIAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0,5, 0.5, 0.5, 1.0))

    def run(self):

        while True:
            self.light_engine.enable()
            self.event_manager.update(self)
            self.update()
            if not self.in_menu():
                self.light_engine.light_interaction(self.game_scene.light_interaction())
                self.light_engine.fire()
            else:
                self.light_engine.menu_light()
            self.light_engine.disable()
            self.try_game_over()

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
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
        self.jump_ratio = 1.25

    def set_easy(self):
        self.game_speed = 1.0
        self.game_block_ratio = 1.0
        self.jump_ratio = 1.0

    def set_hard(self):
        self.game_speed = 4.0
        self.game_block_ratio = 0.2
        self.jump_ratio = 1.7

    def start_game(self):
        self.game_scene.set_difficulty(self.game_speed, self.game_block_ratio, self.jump_ratio)
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
        self.light_engine.reestart()

    def try_game_over(self):
        if self.game_scene.actor.is_game_over():
            self.game_over_scene.point_message.update(self.game_scene.rodillo.points)
            self.actual_scene = self.game_over_scene
            self.event_manager.in_menu = True
            self.light_engine.reestart()
