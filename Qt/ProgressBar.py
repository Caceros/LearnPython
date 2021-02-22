from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def update():
    value = prog_bar.value()
    prog_bar.setValue(value + 1)
 
def reset():
    value = 0
    prog_bar.setValue(value)
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
prog_bar = QtWidgets.QProgressBar(win)
prog_bar.setRange(0, 10)
prog_bar.setGeometry(50, 50, 250, 30)
prog_bar.setValue(0)
 
button = QtWidgets.QPushButton(win)
button.setText("Update")
button.clicked.connect(update)
button.move(50,100)
 
reset_button = QtWidgets.QPushButton(win)
reset_button.setText("Reset")
reset_button.clicked.connect(reset)
reset_button.move(50, 150)
 
win.show()
sys.exit(app.exec_())