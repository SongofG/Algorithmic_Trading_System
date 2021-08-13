# In this file, We are going to try open a window with a message saying "Hello PyQt"
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  # An instance of QApplication class.
# label = QLabel("Hello PyQt")  # Printing the message inside the window.
# print(sys.argv)  # sys.argv == the absolute path of this source code.
label = QPushButton("Quit")  # Pressing the button will not close the window, though it says "Quit".
label.show()
app.exec_()  # This is an infinite loop that is not ended before the users close the window.
