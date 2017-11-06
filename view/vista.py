from controler.game_driver import GameDriver


class Vista:
    def update(self, game_driver: GameDriver):
        """
        dibuja los elementos que necesitan ser nuevamente dibujados en la nueva escena.
        :param game_driver: la instancia del juego completo que se busca dibujar
        :return:
        """
        list_of_changes = game_driver.get_changed()
        self.draw(list_of_changes)

    def draw(self, list_of_changes):
        pass
