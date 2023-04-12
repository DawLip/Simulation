import tkinter as tk

from OpenGL import GL, GLU
from pyopengltk import OpenGLFrame
from OpenGL.GL import *
from OpenGL.GLU import *

class SimulationWindow(OpenGLFrame):
    # def __init__(self, parent, **args):
    #     super().__init__(parent, **args)

    def initgl(self):
        glViewport(0, 0, self.width, self.height)
        
        gluPerspective(90, (1500/750), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glClearColor(0.0, 0.0, 0.0, 0.0) 

    def redraw(self):
        # GL.glRotatef(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_POLYGON)
        glVertex2i(0,0)
        glVertex2i(1,0)
        glVertex2i(1,1)
        glVertex2i(0,1)
        glEnd()

        # glGenTextures(1, &m_texname)
        # glBindTexture(GL_TEXTURE_2D, m_texname)

        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 64, 64, 0, GL_BGR_EXT, GL_UNSIGNED_BYTE, m_image[0])
        

