from controler.event_manager import EventManager
from controler.menus import PauseMenu, StartMenu
from controler.sound_manager import SoundManager
from model.game import Game
from view.vista import Vista


class GameDriver:
    """
    clase para administrar las diferentes facetas del juego.
    """

    def __init__(self):
        self.game = Game()
        self.vista = Vista()
        self.event_manager = EventManager()
        self.sound_manager = SoundManager()
        self.start_menu = StartMenu()
        self.pause_menu = PauseMenu()
        self.actual_menu = self.start_menu

    def start(self):
        """
        inicializa las diferentes facetas del juego y comienza un loop del juego en el menu de inicio
        :return:
        """
        self.event_manager.set_in_menu()
        while self.event_manager.in_menu():
            self.event_manager.update()
            self.vista.show_menu(self.start_menu)

    def run(self):
        while True:
            self.event_manager.update(self)
            self.game.update()
            self.vista.update()

    def set_in_pause(self):
        self.event_manager.set_in_menu()
