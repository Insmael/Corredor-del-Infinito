from random import randint

from OpenGL.GL import *

from view.elements.blockstyle import BlockStyle
from view.vertex_generator import Vertex_generator


class Scene:
    def __init__(self):
        self.context = None  # el fondo del juego, podria ser un sprite, o una textura.
        self.rot = 0.0
        self.faces = 8
        self.delta_ang = 360.0 / self.faces
        deep = 5
        self.slices = []
        self.vert_gen = Vertex_generator(1, self.faces, 0.2, 2)
        for i in range(20):
            figures = []
            self.vert_gen.define(1, self.faces, 0.2, deep * i)
            centers_pos = self.vert_gen.centers_pos()
            rot_angs = self.vert_gen.rot_angs()
            all_vert = self.vert_gen.all_body_verteces(deep - 1)
            for i in range(self.faces):
                b = BlockStyle()
                b.set_rot_ang(rot_angs[i])
                b.set_pos(centers_pos[i][0], centers_pos[i][1], centers_pos[i][2])
                b.def_vertices(all_vert)
                figures.append(b)
            self.slices.append(figures)
        self.make_random()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for slice in self.slices:
            for fig in slice:
                fig.draw(self.rot)

    def rot_left(self):
        self.rot += self.delta_ang

    def rot_right(self):
        self.rot -= self.delta_ang

    def make_random(self):
        for slice in self.slices:
            k = randint(0, self.faces)
            for i in range(k):
                slice.pop(randint(0, len(slice) - 1))
