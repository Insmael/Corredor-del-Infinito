import os

import pygame
import pygame.image
from OpenGL.GL import *
from OpenGL.GLU import *

from model.axis import Axis


class Other:
    def __init__(self):
        self.pos = [0.0, 0.0, 0.0]

    def new_pos(self, pos):
        self.pos = pos

    def draw(self):
        pass


class GameOverMessage(Other):
    def __init__(self):
        super(GameOverMessage, self).__init__()
        self.message = (SimpleTexture('g', (-11.0, 2.0, -20.0)),
                        SimpleTexture('a', (-8.0, 2.0, -20.0)),
                        SimpleTexture('m', (-5.0, 2.0, -20.0)),
                        SimpleTexture('e', (-2.0, 2.0, -20.0)),
                        SimpleTexture('o', (2.0, 2.0, -20.0)),
                        SimpleTexture('v', (5.0, 2.0, -20.0)),
                        SimpleTexture('e', (8.0, 2.0, -20.0)),
                        SimpleTexture('r', (11.0, 2.0, -20.0)))
        self.new_pos((0.0, 1.0, 0.0))

    def draw(self):
        for letter in self.message:
            glLoadIdentity()
            glTranslatef(self.pos[Axis.X], self.pos[Axis.Y], self.pos[Axis.Z])
            letter.draw()


class SimpleTexture:
    def __init__(self, nombre, pos=(0.0, 0.0, 0.0)):
        self.texture = self.load_texture(nombre + '.bmp')
        self.pos = pos

    def draw(self):
        glTranslatef(self.pos[Axis.X], self.pos[Axis.Y], self.pos[Axis.Z])
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
