# In PyQt, we call the bottom most widget, not contained in other widgets, a window.

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):  # Inheriting from QMainWindow Class
    def __init__(self):
        super().__init__()  # Calls __init__() from the parent class
        self.setWindowTitle("PyStock")  # Name the window to be "PyStock"
        self.setGeometry(300, 300, 300, 400)  # Set the size of the window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
