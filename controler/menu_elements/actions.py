class Action:
    def texture_name(self):
        return 'galaxia1'

    def act(self):
        pass

class EasyDifficulty(Action):
    def texture_name(self):
        return 'facil'


class MediumDifficulty(Action):
    def texture_name(self):
        return 'media'


class HardDifficulty(Action):
    def texture_name(self):
        return 'dificil'


class Continue(Action):
    def texture_name(self):
        return 'reanudar'


class StartGame(Action):
    def texture_name(self):
        return 'comenzar'


class CloseGame(Action):
    def texture_name(self):
        return 'salir'


class GoMenu(Action):
    def texture_name(self):
        return 'IrAlMenu'
