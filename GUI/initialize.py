import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import random
import copy

sys.path.insert(1, os.path.abspath('.'))
from data import data, toQImg, GUIData

def initializeGUI(window, app):
    global label
    global label2

    window.setWindowTitle("Sim")
    window.setGeometry(0,0,data["x"],data["y"])

    GUIData['map'] = QLabel(window, alignment=Qt.AlignCenter)
    GUIData['map'].setPixmap(QPixmap(toQImg()))
    window.setCentralWidget(GUIData['map'])

    GUIData['ticks'] = QLabel(window, text=str(data["tick"]), alignment=Qt.AlignCenter)
    GUIData['ticks'].setText(str(data["tick"]))
    
    window.show()