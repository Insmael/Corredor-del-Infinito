class Actor:
    """
    representación del actor en el juego.
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z

    def jumping(self):
        pass

    def stop_jumping(self):
        pass
