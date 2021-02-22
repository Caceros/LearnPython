from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,500,300)
win.setWindowTitle("CodersLegacy")
 
button = QtWidgets.QPushButton(win)
button.clicked.connect(win.close)
button.setText("Quit Button")
button.resize(120,60)
button.move(350,220)
 
win.show()
sys.exit(app.exec_())