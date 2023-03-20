import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import random
import copy

from initialize import initializeGUI
from render import render

def GUI():
    app = QApplication(sys.argv)
    window = QMainWindow()

    initializeGUI()
    
    timer = QTimer()
    timer.singleShot(0, render())

    sys.exit(app.exec())