import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import threading as th
import platform as p

separator = "\\" if p.system() == "Windows" else "/"  #separator of file system

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi(".{0}gui{0}main_window.ui".format(separator), self)
        self.load_css()

    def load_css(self):
        with open(".{0}css{0}main_window_style.css".format(separator)) as myCSSfile:
            myCSS = myCSSfile.read()
            self.setStyleSheet(myCSS)

# Driver code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())