from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def display():
    print(dial.value())
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
dial = QtWidgets.QDial(win)
dial.setMinimum(0)
dial.setMaximum(100)
dial.move(100,50)
 
dial.valueChanged.connect(display)
 
win.show()
sys.exit(app.exec_())