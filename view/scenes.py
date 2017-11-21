from model.menu_elements.actions import *
from model.menu_elements.button import Button

from model.menu_elements.others import *
from model.rodillo import Rodillo
from view.context import Context
from view.elements.actorStyle import ActorHomoMorfo


class GameScene:
    def __init__(self):
        self.context = Context()
        self.rodillo = Rodillo()
        self.actor_deep = -0.7
        # self.actor = Actor([0.0, -0.15, self.actor_deep])

        # segunda imagen de actor, sobree escribe a la anterior
        self.actor = ActorHomoMorfo([0.0, -0.15, self.actor_deep])

    def reestart(self):
        self.__init__()

    def set_difficulty(self, game_speed, block_ratio, jump_ratio):
        self.rodillo.speed *= game_speed
        self.rodillo.block_ratio *= block_ratio
        self.actor.jump_ratio = jump_ratio

    def draw(self):
        self.context.draw()
        self.rodillo.draw()
        self.rodillo.draw_points()
        self.actor.draw(self.rodillo.speed)

        if self.rodillo.is_standable(self.actor_deep, self.actor.is_standing()):
            self.actor.stop_falling()
        else:
            self.actor.normal_fall()

    def light_interaction(self):
        if self.rodillo.lights_on():
            self.rodillo.switch_lights()
            return True
        return False

    def jump_left(self):
        if not self.actor.moving():
            self.actor.set_jumping(self.rodillo.is_standable(self.actor_deep, self.actor.is_standing()))
            self.rodillo.rot_left()

    def jump_right(self):
        if not self.actor.moving():
            self.actor.set_jumping(self.rodillo.is_standable(self.actor_deep, self.actor.is_standing()))
            self.rodillo.rot_right()

    def jump_straight(self):
        self.actor.set_jumping(self.rodillo.is_standable(self.actor_deep, self.actor.is_standing()))

    def fall(self):
        self.actor.fall()


class MenuScene:
    def __init__(self):
        self.context = Context()
        self.buttons = {}
        self.button_keys = []

    def reestart(self):
        self.__init__()

    def draw(self):
        self.context.draw()
        for key in self.button_keys:
            self.buttons[key].draw()


class MainMenuScene(MenuScene):
    def __init__(self):
        super(MainMenuScene, self).__init__()
        self.buttons = {'start': Button(StartGame(), (-5.0, 0.0, -12.0)),
                        'close': Button(CloseGame(), (5.0, 0.0, -12.0)),
                        'easy': Button(EasyDifficulty(), (0.0, 0.0, -12.0)),
                        'medium': Button(MediumDifficulty(), (0.0, 0.0, -12.0)),
                        'hard': Button(HardDifficulty(), (0.0, 0.0, -12.0))}
        self.difficulties = ['easy', 'medium', 'hard']
        self.button_keys = ['start', 'easy', 'close']
        self.over = 0
        self.change_over()

    def select(self, vista):
        if self.over == 1:
            self.next_dificulty()
        self.buttons[self.button_keys[self.over]].select(vista)

    def next_dificulty(self):
        if self.button_keys[1] == 'easy':

            self.button_keys[1] = 'medium'
        else:
            if self.button_keys[1] == 'medium':
                self.button_keys[1] = 'hard'
            else:
                if self.button_keys[1] == 'hard':
                    self.button_keys[1] = 'easy'

    def next_item(self):
        self.change_over()
        if self.over == 2:
            self.over = 0
        else:
            self.over += 1
        self.change_over()

    def before_item(self):
        self.change_over()
        if self.over == 0:
            self.over = 2
        else:
            self.over -= 1
        self.change_over()

    def change_over_dificulties(self):
        for difficulty in self.difficulties:
            self.buttons[difficulty].change_over()

    def change_over(self):
        if self.over == 1:
            self.change_over_dificulties()
        else:
            self.buttons[self.button_keys[self.over]].change_over()


class GameOverScene(MenuScene):
    def __init__(self):
        super(GameOverScene, self).__init__()
        self.buttons = {'goMenu': Button(GoMenu(), (0.0, -1.0, -12.0))}
        self.button_keys = ['goMenu']
        self.over = 0
        self.change_over()
        self.context = Context()
        self.game_over_message = GameOverMessage()

    def draw(self):
        self.context.draw()
        for key in self.button_keys:
            self.buttons[key].draw()
        self.game_over_message.draw()

    def select(self, vista):
        self.buttons[self.button_keys[self.over]].select(vista)

    def next_item(self):
        pass

    def before_item(self):
        pass

    def change_over(self):
        self.buttons[self.button_keys[self.over]].change_over()


class PauseScene(MenuScene):
    def __init__(self):
        super(PauseScene, self).__init__()
        self.buttons = {'continue': Button(Continue(), (-3.0, 0.0, -12.0)),
                        'goMenu': Button(GoMenu(), (3.0, 0.0, -12.0))}
        self.button_keys = ['continue', 'goMenu']
        self.over = 0
        self.change_over()
        self.context = Context()

    def select(self, vista):
        self.buttons[self.button_keys[self.over]].select(vista)

    def next_item(self):
        self.change_over()
        if self.over:
            self.over = 0
        else:
            self.over = 1
        self.change_over()

    def before_item(self):
        self.next_item()

    def change_over(self):
        self.buttons[self.button_keys[self.over]].change_over()
