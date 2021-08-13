#

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")  # A method from the parent class
        self.setGeometry(300, 300, 300, 400)  # A method from the parent class

        btn1 = QPushButton("Click Me", self)  # An instance of QPushButton
        btn1.move(20, 20)  # Set the position of the button
        btn1.clicked.connect(self.btn1_clicked)  # When clicked, calls btn1_clicked().

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")  # "message" = widget name. "clicked" = message shown.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
