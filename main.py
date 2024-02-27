# print('-'*55)
import os #------------------ бібліотека інформаційна  система

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
from PyQt5.QtWidgets import QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import BLUR, DETAIL

class ImageProcessor:
    def __init__(self):
        pass

    def load_image(self,filename):
        pass

    def save_image(self):
        pass

app = QApplication()
win = QWidget()
win.resize(1200, 750)
win.setWindowTitle("Demo Photoshop")

app.exec()






