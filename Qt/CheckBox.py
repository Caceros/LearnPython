from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def show():
    result = combo.currentText()
    print(result)
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
combo = QtWidgets.QComboBox(win)
combo.addItems(["Python", "Java", "C++"])
combo.move(100,100)
 
button = QtWidgets.QPushButton(win)
button.setText("Submit")
button.clicked.connect(show)
button.move(100,200)
 
win.show()
sys.exit(app.exec_())