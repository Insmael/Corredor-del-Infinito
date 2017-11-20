from math import cos, sin, radians

import pygame
from OpenGL.GL import *

from controler.menu_elements.others import PointMessage
from model.map_element import *
from view.vertex_generator import Vertex_generator


class Rodillo:
    """
    una lista con los elementos que tiene el mapa
    """

    def __init__(self):

        # construcción del mapa
        self.block_ratio = -3
        self.faces = 8
        self.deep = 5
        self.slices = []
        self.vert_gen = Vertex_generator(1, self.faces, 0.2, 2)
        for i in range(9):
            self.create_slice(i)
        self.make_random()

        # dibujar el mapa
        self.render_deepness = 0.0
        self.speed = 0.1
        self.rot = -90.0
        self.delta_ang = 360.0 / self.faces

        # otros
        self.points = 0
        self.point_message = PointMessage()
        self.light_switch = False

    def create_slice(self, i):  # slices
        figures = []
        self.vert_gen.define(1, self.faces, 0.2, self.deep * i)
        centers_pos = self.vert_gen.centers_pos()
        rot_angs = self.vert_gen.rot_angs()
        all_vert = self.vert_gen.all_body_verteces(self.deep)
        for j in range(self.faces):
            b = Block()
            b.set_rot_ang(rot_angs[j])
            b.set_pos(centers_pos[j][0], centers_pos[j][1])
            b.def_vertices(all_vert)
            figures.append(b)
        self.slices.append(figures)

    def draw(self):  # general
        z_pos = self.render_deepness
        for a_slice in self.slices:
            z_pos -= self.deep
            for fig in a_slice:
                fig.draw(self.rot, z_pos)
        self.render_deepness += self.speed
        self.send_back()

    def rot_left(self):  # mecanicas
        self.rot += self.delta_ang

    def rot_right(self):  # mecanicas
        self.rot -= self.delta_ang

    def make_random(self):  # todas las slices
        for i in range(2, len(self.slices)):
            self.remake_random(self.slices[i])

    def remake_random(self, a_slice):  # una slice
        k = max(0, randint(int(self.block_ratio), self.faces))
        for i in range(k):
            a_slice.pop(randint(0, len(a_slice) - 1))

    def send_back(self):  # una slice
        if self.render_deepness > self.deep * 2:
            self.render_deepness -= self.deep
            self.create_slice(len(self.slices))
            self.slices.pop(0)
            self.remake_random(self.slices[-1])

    def is_standable(self, actor_deep, standing):  # mecanicas
        actual_slice = int((self.render_deepness - actor_deep * (1.5) + self.deep) / self.deep - 1)
        for fig in self.slices[actual_slice]:
            c_x, c_y = fig.get_center()
            x = c_y * sin(-radians(self.rot)) + c_x * cos(radians(self.rot))
            y = c_x * sin(radians(self.rot)) + c_y * cos(-radians(self.rot))
            if abs(x) < 0.01:
                if y < 0:
                    if standing:
                        fig.interact(self)
                    return True
        return False

    def draw_text(self, x, y, text, color=(255, 255, 255, 0), fondo=(0, 0, 0, 0), tamaño=25):  # extra
        position = (x, y, 0.0, 0.0)
        font = pygame.font.Font(None, tamaño)
        text_surface = font.render(text, True, color, fondo)
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        glTranslatef(10, 5, 0.0)
        glRasterPos4f(*position)
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    def light_effect(self):
        self.light_switch = not self.light_switch

    def draw_points(self):
        self.points += self.speed * 2
        self.point_message.update(self.points)
        self.point_message.draw()
