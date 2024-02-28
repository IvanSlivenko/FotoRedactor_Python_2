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

    def b_w(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def do_flip(self):
        pass

    def do_blur(self):
        pass

def filter_images(files,extensions):
    """esult=[]
    for filename in files:
        for ext in extensions:
          if filename.endswith(ext):
              result.append(filename)
    return result"""

# --------- або
    return [filename for filename in files for ext in extensions if filename.endswith(ext)]






def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def show_filenames_list():
    extensions = ['.jpg', 'jpeg', 'png', 'bmp', 'gif']
    choose_workdir()
    filenames = filter_images(os.listdir(workdir),extensions)

def show_info():
    my_info = QMessageBox()
    my_info.setText('Demo Photoshop\nVer.1.0=)')

workdir = ''

app = QApplication()
win = QWidget()
win.resize(1200, 750)
win.setWindowTitle("Demo Photoshop")

btn_dir = QPushButton('Директорія')
lb_image =QLabel('Зображення')
btn_files = QListWidget()

btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
btn_flip = QPushButton('flip')
btn_sharp = QPushButton('Sharp')
btn_b_w = QPushButton('B / W')
btn_blur = QPushButton('Blur')
btn_contour = QPushButton('Contour')
btn_detail = QPushButton('Detail')

btn_info = QPushButton('INFO')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(btn_files)
col2.addWidget(lb_image, 95)
col2.addWidget(btn_info)

row_tools1 = QHBoxLayout()
row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_flip)
row_tools1.addWidget(btn_sharp)
row_tools1.addWidget(btn_b_w)
row_tools1.addWidget(btn_contour)
row_tools1.addWidget(btn_detail)

col2.addLayout(row_tools1)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)

app.exec()






