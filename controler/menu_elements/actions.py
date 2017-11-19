import pygame


class Action:
    def texture_name(self):
        return 'galaxia1'

    def act(self, vista):
        pass


class EasyDifficulty(Action):
    def texture_name(self):
        return 'facil'

    def act(self, vista):
        vista.set_easy()


class MediumDifficulty(Action):
    def texture_name(self):
        return 'media'

    def act(self, vista):
        vista.set_medium()


class HardDifficulty(Action):
    def texture_name(self):
        return 'dificil'

    def act(self, vista):
        vista.set_hard()


class Continue(Action):
    def texture_name(self):
        return 'reanudar'

    def act(self, vista):
        vista.set_unpause()


class StartGame(Action):
    def texture_name(self):
        return 'comenzar'

    def act(self, vista):
        vista.start_game()


class CloseGame(Action):
    def texture_name(self):
        return 'salir'

    def act(self, vista):
        pygame.quit()

class GoMenu(Action):
    def texture_name(self):
        return 'IrAlMenu'

    def act(self, vista):
        vista.set_main_menu()
