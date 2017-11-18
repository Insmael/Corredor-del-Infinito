from random import randint

from controler.menu_elements.actions import *
from controler.menu_elements.button import Button
from model.rodillo import Rodillo
from view.context import Context
from view.elements.actorStyle import RectangleActor


class Scene:
    def __init__(self):
        self.context = Context()
        self.rodillo = Rodillo()
        self.actor_deep = -0.7
        self.actor = RectangleActor([0.0, -0.15, self.actor_deep])

    def draw(self):
        self.context.draw()
        self.rodillo.draw()
        self.actor.draw()

        if self.rodillo.is_standable(self.actor_deep):
            self.actor.stop_falling()
        else:
            self.actor.normal_fall()

    def jump_left(self):
        if not self.actor.moving():
            self.actor.set_jumping(self.rodillo.is_standable(self.actor_deep))
            self.rodillo.rot_left()

    def jump_right(self):
        if not self.actor.moving():
            self.actor.set_jumping(self.rodillo.is_standable(self.actor_deep))
            self.rodillo.rot_right()

    def jump_straight(self):
        self.actor.set_jumping(self.rodillo.is_standable(self.actor_deep))

    def fall(self):
        self.actor.fall()


class MenuScene:
    def __init__(self):
        self.dificulty_buttons = (Button(EasyDifficulty(), (0.0, 0.0, -12.0)),
                                  Button(MediumDifficulty(), (0.0, 0.0, -12.0)),
                                  Button(HardDifficulty(), (0.0, 0.0, -12.0)))
        self.actual_difficulty = self.dificulty_buttons[0]
        self.default_buttoms = [Button(StartGame(), (-5.0, 0.0, -12.0)), self.actual_difficulty,
                                Button(CloseGame(), (5.0, 0.0, -12.0))]

        self.context = Context()
        self.over = 1
        self.default_buttoms[self.over].change_over()

    def draw(self):
        self.context.draw()
        self.actual_difficulty = self.dificulty_buttons[randint(0, 2)]
        for buttons in self.default_buttoms:
            buttons.draw()

    def set_easy(self):
        self.actual_difficulty = self.dificulty_buttons[0]

    def set_medium(self):
        self.actual_difficulty = self.dificulty_buttons[1]

    def set_hard(self):
        self.actual_difficulty = self.dificulty_buttons[2]

    def select(self):
        self.default_buttoms[self.over].select()
