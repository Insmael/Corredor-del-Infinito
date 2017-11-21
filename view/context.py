import os

import pygame
import pygame.image
from OpenGL.GL import *
from OpenGL.GLU import *


class Context:
    def __init__(self):
        self.textures = self.load('galaxia3.bmp')

    def load(self, file):
        texturefile = os.path.join('view', 'textures', file)
        textureSurface = pygame.image.load_extended(texturefile)
        textureData = pygame.image.tostring(textureSurface, "RGBX", 1)
        textures = glGenTextures(3)

        glBindTexture(GL_TEXTURE_2D, textures[0])
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(), 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glBindTexture(GL_TEXTURE_2D, textures[1])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(), 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glBindTexture(GL_TEXTURE_2D, textures[2])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(),
                          GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        return textures

    def draw(self):
        glLoadIdentity()
        glColor3fv((10, 10, 10))
        glTranslatef(0.0, 0.0, -100.0)
        glScalef(50.0, 40.0, 0.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.textures[2])
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
