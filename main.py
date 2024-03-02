# print('-'*55)
import os #------------------ бібліотека інформаційна  система

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
from PyQt5.QtWidgets import QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import BLUR, DETAIL, SMOOTH, CONTOUR, SHARPEN, \
EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, UnsharpMask

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified'


    def load_image(self,filename):
        self.filename = filename
        # fullname = os.path.join(workdir, filename)
        self.image = Image.open(os.path.join(workdir, filename))

    def save_image(self):
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)

        self.image.save(fullname)

    def b_w(self):
        self.image = self.image.convert('L')
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)




    def turn_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def turn_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_blur(self):
        self.image = self.image.transpose(BLUR)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_sharpen(self):
        self.image = self.image.transpose(SHARPEN)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
    def do_contour(self):
        self.image = self.image.transpose(CONTOUR)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
    def do_detail(self):
        self.image = self.image.transpose(DETAIL)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
    def do_smoth(self):
        self.image = self.image.transpose(SMOOTH)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_emboss(self):
        self.image = self.image.transpose(EMBOSS)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_edge_enhance(self):
        self.image = self.image.transpose(EDGE_ENHANCE)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def show_image(self):
        pass


def filter_images(files, extensions):
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



def show_shosen_image():
    if btn_files.currentRow() >= 0:
        filename = btn_files.currentItem().text()







workdir = ''

app = QApplication([])
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

workimage = ImageProcessor()
btn_files.currentRowChanged.connect(show_shosen_image)

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

row_tools2 = QHBoxLayout()
row_tools2.addWidget(btn_left)
row_tools2.addWidget(btn_right)
row_tools2.addWidget(btn_flip)
row_tools2.addWidget(btn_sharp)
row_tools2.addWidget(btn_b_w)
row_tools2.addWidget(btn_contour)
row_tools2.addWidget(btn_detail)

col2.addLayout(row_tools1)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)

app.exec()






