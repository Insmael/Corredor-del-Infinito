class Effect:
    pass


class NullEffect(Effect):
    def __str__(self):
        return "Effect:Normal"

    def interact(self, rodillo):
        pass


class SpeedUpEffect(Effect):
    def __str__(self):
        return "Effect:SpeedUp"

    def interact(self, rodillo):
        rodillo.speed *= 1.005


class SpeedDownEffect(Effect):
    def __str__(self):
        return "Effect:SpeedDown"

    def interact(self, rodillo):
        rodillo.speed *= 0.995


class LightChangeEffect(Effect):
    def __str__(self):
        return "Effect:LightChange"

    def interact(self, rodillo):
        pass

class PointEffect(Effect):
    def __str__(self):
        return "Effect:Points"

    def interact(self, rodillo):
        pass
