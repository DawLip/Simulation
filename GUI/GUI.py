import os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import random
import copy

from GUI.initialize import initializeGUI
from GUI.render import renderMap

sys.path.insert(1, os.path.abspath('.'))
from data import GUIData

def GUI():
    app = QApplication(sys.argv)
    window = QMainWindow()

    initializeGUI(window, app)

    GUIData['timer'] = QTimer()
    GUIData['timer'].singleShot(1, renderMap)

    sys.exit(app.exec())