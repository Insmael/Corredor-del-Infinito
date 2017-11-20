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
    def __init__(self):
        self.activable = True

    def __str__(self):
        return "Effect:LightChange"

    def interact(self, rodillo):
        if self.activable:
            rodillo.light_effect()
            self.activable = False

class PointEffect(Effect):
    def __init__(self):
        self.activable = True

    def __str__(self):
        return "Effect:Points"

    def interact(self, rodillo):
        def interact(self, rodillo):
            if self.activable:
                rodillo.light_effect()
                self.activable = False
