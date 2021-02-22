from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import sys
 
def display():
    my_label.setText(str(slider.value()))
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
slider = QtWidgets.QSlider(Qt.Horizontal, win)
slider.setGeometry(50,50, 200, 50)
slider.setMinimum(0)
slider.setMaximum(20)
slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
slider.setTickInterval(2)
slider.valueChanged.connect(display)
 
my_label = QtWidgets.QLabel(win)
my_label.move(100, 100)
 
win.show()
sys.exit(app.exec_())