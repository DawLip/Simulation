import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import random
import copy

def initializeGUI(app, window):
    global label
    global label2

    window.setWindowTitle("Sim")
    window.setGeometry(0,0,data["x"],data["y"])

    label = QLabel(window, alignment=Qt.AlignCenter)
    label.setPixmap(QPixmap(toQImg()))
    window.setCentralWidget(label)

    label2 = QLabel(window, text=str(data["tick"]), alignment=Qt.AlignCenter)
    label2.setText(str(data["tick"]))
    
    window.show()