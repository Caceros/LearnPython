from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
 
def show_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Message Box")
    msg.setText("This is some random text")
     
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Cancel)
    msg.setDetailedText("Details display here")
    msg.setInformativeText("This is some extra information")
    msg.buttonClicked.connect(popup)
     
    x = msg.exec_()
 
def popup(i):
    print(i.text())
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
button = QtWidgets.QPushButton(win)
button.setText("A Button")
button.clicked.connect(show_popup)
button.move(100,100)
 
win.show()
sys.exit(app.exec_())