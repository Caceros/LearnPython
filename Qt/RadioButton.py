from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
import sys
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")

layout = QGridLayout()

def on_toggle():
    print(f'{radio.text()} checked: {radio.isChecked()}')

radio = QtWidgets.QRadioButton(win)
radio.setText("Option1")
radio.move(50,100)
layout.addWidget(radio, 0, 0)
radio.toggled.connect(on_toggle)
 
radio2 = QtWidgets.QRadioButton(win)
radio2.setText("Option2")
radio2.move(50,150)
layout.addWidget(radio, 0, 1)
 
win.show()
sys.exit(app.exec_())