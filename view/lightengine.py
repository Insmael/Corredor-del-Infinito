from random import gauss, randint

from OpenGL.GL import *


class LightEnginne:
    def __init__(self):
        # camara
        self.camPos = (0, 0, 0)
        self.camAt = (0, 0, 0)

        # luz
        self.light = GL_LIGHT0
        self.l_position = (10.0, 1.0, -0.1, 1.0)

        # crear una luz coherente con su color base
        self.l_diffuse = [5.0, 5.0, 5.0, 1.0]
        self.l_ambient = [i / 8.0 for i in self.l_diffuse]
        self.l_specular = self.l_diffuse

        # otros valores estandar
        self.l_constant_attenuation = 1.0
        self.l_linear_attenuation = 0.2
        self.l_quadratic_attenuation = 0.01

        self.l_spot_cutoff = 180.0
        self.l_spot_direction = (0.0, 10.0, -0.5)  # direccion
        self.l_spot_exponent = 1.0

        # effectors
        self.l_eff_manager = LEffmanager()

    def fire(self):
        self.static_fire()

    def static_fire(self):
        glLoadIdentity()
        # gluLookAt(self.camPos[0], self.camPos[1], self.camPos[2],  # posicion
        #          self.camAt[0], self.camAt[1], self.camAt[2],  # mirando hacia
        #          0.0, 0.0, 1.0)  # inclinacion

        # luz
        self.l_eff_manager.aply_effect()
        glLightfv(self.light, GL_POSITION, self.l_eff_manager.l_position())
        glLightfv(self.light, GL_AMBIENT, self.l_eff_manager.l_ambient())
        glLightfv(self.light, GL_SPECULAR, self.l_eff_manager.l_specular())
        glLightfv(self.light, GL_DIFFUSE, self.l_eff_manager.l_diffuse())

        glLightf(self.light, GL_CONSTANT_ATTENUATION, self.l_eff_manager.l_constant_attenuation())
        glLightf(self.light, GL_LINEAR_ATTENUATION, self.l_eff_manager.l_linear_attenuation())
        glLightf(self.light, GL_QUADRATIC_ATTENUATION, self.l_eff_manager.l_quadratic_attenuation())
        glLightf(self.light, GL_SPOT_CUTOFF, self.l_spot_cutoff)
        glLightfv(self.light, GL_SPOT_DIRECTION, self.l_spot_direction)
        glLightf(self.light, GL_SPOT_EXPONENT, self.l_spot_exponent)

    def menu_light(self):
        glLoadIdentity()
        # gluLookAt(self.camPos[0], self.camPos[1], self.camPos[2],  # posicion
        #          self.camAt[0], self.camAt[1], self.camAt[2],  # mirando hacia
        #          0.0, 0.0, 1.0)  # inclinacion

        # luz
        glLightfv(self.light, GL_POSITION, (1.0, 1.0, -10.1, 0.0))
        glLightfv(self.light, GL_AMBIENT, self.l_ambient)

    def enable(self):
        glEnable(self.light)

    def disable(self):
        glDisable(self.light)

    def light_interaction(self, bool):
        if bool:
            self.l_eff_manager.switch_effects()


class LightEffect:
    def __init__(self):
        self.l_position = (10.0, 1.0, -0.1, 1.0)

        # crear una luz coherente con su color base
        self.l_diffuse = [5.0, 5.0, 5.0, 1.0]
        self.l_ambient = [i / 8.0 for i in self.l_diffuse]
        self.l_specular = self.l_diffuse

        self.l_constant_attenuation = 1.0
        self.l_linear_attenuation = 0.2
        self.l_quadratic_attenuation = 0.01

    def aply(self):
        pass


class NullLightEffect(LightEffect):
    def aply(self):
        pass


class MovingLightEffect(LightEffect):
    def aply(self):
        self.l_position = [min(3, max(-3, gauss(0, 0.001) + x)) for x in self.l_position]


class ColorLightEffect(LightEffect):
    def aply(self):
        self.l_diffuse = [min(3, max(-3, gauss(0, 0.001) + x)) for x in self.l_diffuse]


class PumpingLightEffect(LightEffect):
    def aply(self):
        self.l_constant_attenuation = min(3, max(0, gauss(0, 0.001) + self.l_constant_attenuation))
        self.l_linear_attenuation = min(0.2, max(0, gauss(0, 0.001) + self.l_linear_attenuation))
        self.l_quadratic_attenuation = min(0.2, max(0, gauss(0, 0.001) + self.l_quadratic_attenuation))


class LEffmanager:
    def __init__(self):
        self.no_effect = NullLightEffect()
        self.effects = [MovingLightEffect(), ColorLightEffect(), PumpingLightEffect()]
        self.effect_on = False
        self.actual = self.no_effect

    def aply_effect(self):
        self.actual.aply()

    def l_position(self):
        return self.actual.l_position

    def l_ambient(self):
        return self.actual.l_ambient

    def l_diffuse(self):
        return self.actual.l_diffuse

    def l_specular(self):
        return self.actual.l_specular

    def l_constant_attenuation(self):
        return self.actual.l_constant_attenuation

    def l_linear_attenuation(self):
        return self.actual.l_linear_attenuation

    def l_quadratic_attenuation(self):
        return self.actual.l_quadratic_attenuation

    def switch_effects(self):
        if self.effect_on:
            self.actual = self.no_effect
            self.effect_on = False

        else:
            self.actual = self.effects[randint(0, 2)]
            self.effect_on = True
