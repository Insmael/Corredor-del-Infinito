from model.rodillo import Rodillo


class Mapa:
    """
    representación del mapa en el juego
    """

    def __init__(self):
        self.rodillo = Rodillo()

    def rotar_izq(self):
        self.rodillo.rotar_izq()

    def rotar_der(self):
        self.rodillo.rotar_der()
