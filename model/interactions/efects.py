class Effect:
    pass


class NullEffect(Effect):
    def __str__(self):
        return "Effect:Normal"


class SpeedUpEffect(Effect):
    def __str__(self):
        return "Effect:SpeedUp"


class SpeedDownEffect(Effect):
    def __str__(self):
        return "Effect:SpeedDown"


class LightChangeEffect(Effect):
    def __str__(self):
        return "Effect:LightChange"


class PointEffect(Effect):
    def __str__(self):
        return "Effect:Points"
