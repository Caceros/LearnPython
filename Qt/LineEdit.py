from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def show():
    print(line.text())

def changed(text: str):
    print(text)

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
line = QtWidgets.QLineEdit(win)
line.setFixedWidth(140)
line.move(80,80)
line.textChanged.connect(changed)

button = QtWidgets.QPushButton(win)
button.setText("Submit")
button.clicked.connect(show)
button.move(100,150)
 
button = QtWidgets.QPushButton(win)
button.setText("Clear")
button.clicked.connect(line.clear)
button.move(100,220)

win.show()
sys.exit(app.exec_())