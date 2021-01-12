from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main_view import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import qdarkstyle
import pickle
import cv2
from keras.models import load_model
class file_D(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(file_D,self).__init__()
        self.setupUi(self)
        self.show_btn.clicked.connect(lambda : self.show_result())
        self.show()
    def show_result(self):
        filename,_= QFileDialog.getOpenFileName(self,'openfile',r"C:\Users\sch\Documents\python\QT_projects\breast_cancer1\images",'All file(*.*);;Image files (*.jpg *.png)')
        self.img_lbl.setPixmap(QPixmap(filename))
        model = load_model("X-ray_model.hdf5")
        image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (100,100))
        images = image.reshape(-1,100,100,1)
        result = model.predict([images])
        self.set_msg("you are pinomial") if result == 1 else self.set_msg("you are normal")
    def set_msg(self,txt):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("X-ray result")
        msg.setText(txt)
        msg.exec_()
app = QtWidgets.QApplication([])
win_app = file_D()
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
app.exec_()
