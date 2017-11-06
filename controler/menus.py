from controler.menu_elements.actions import *
from controler.menu_elements.button import Button


class Menu:
    def __init__(self):
        self.buttons = []
        self.add_buttons()

    def add_buttons(self):
        b = Button(SetDifficulty())
        self.buttons.append(b)

        b = Button(CloseGame())
        self.buttons.append(b)


class StartMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        b = Button(StartGame())
        self.buttons.append(b)


class PauseMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        b = Button(UnPause())
        self.buttons.append(b)
