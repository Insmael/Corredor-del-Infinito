import os
from math import sin

import pygame
import pygame.image
from OpenGL.GL import *
from OpenGL.GLU import *

from model.axis import Axis


class ButtonStyle:
    def __init__(self, nombre, pos=(0.0, 0.0, 0.0)):
        self.texture = self.load_texture(nombre + '.bmp')
        self.pos = pos
        self.ang = 0
        self.shining = False

    def change_shining(self):
        self.shining = not self.shining

    def draw(self):
        glLoadIdentity()
        glTranslatef(self.pos[Axis.X], self.pos[Axis.Y], self.pos[Axis.Z])
        glRotatef(sin(self.ang), 0.0, 0.0, 1.0)
        glScalef(1.7, 1.0, 0.0)
        if self.shining:
            self.draw_shiness()
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)  # Top Left Of The Texture and Quad
        glEnd()
        glDisable(GL_TEXTURE_2D)
        self.ang = pygame.time.get_ticks() / 500

    def load_texture(self, file):
        texturefile = os.path.join('view', 'wallpapers', file)
        textureSurface = pygame.image.load_extended(texturefile)
        textureData = pygame.image.tostring(textureSurface, "RGBX", 1)
        texture = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(),
                          GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        return texture

    def draw_shiness(self):
        glBegin(GL_QUADS)
        delta = sin(abs(self.ang * 2))
        colors = [y + 1 / 6 * delta for y in [1.0, 0.25, 0.05]]
        glColor3fv(colors)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(-1.05, -1.05, 1.1)  # Bottom Left Of The Texture and Quad
        glVertex3f(1.05, -1.05, 1.1)  # Bottom Right Of The Texture and Quad
        glVertex3f(1.05, 1.05, 1.1)  # Top Right Of The Texture and Quad
        glVertex3f(-1.05, 1.05, 1.1)  # Top Left Of The Texture and Quad
        glEnd()
        # glClearColor(1,1,1,1) linea para ver hasta donde llega la textura de fondo
        glColor3f(1.0, 1.0, 1.0)
