from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QPushButton, QLabel
import sys
 
def display():
    text , pressed = QInputDialog.getText(window, "Input Text", "Text: ",
                                           QLineEdit.Normal, "")
    int_num , pressed = QInputDialog.getInt(window, "Input Integer","Number:",
                                            10, 0, 100, 1)
    options = ("Option1", "Option2", "Option3")                                           
    option , pressed = QInputDialog.getItem(window, "Select Item","Option:",
                                            options, 0, False)
    decimal, pressed = QInputDialog.getDouble(window, "Input Decimal","Value:",
                                            10.00, 0, 100, 2)
    if pressed:
        label.setText(f'{text}/{int_num}/{option}/{decimal}')
        label.adjustSize()

         
app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(400,400,250,250)
window.setWindowTitle("CodersLegacy")
 
label = QLabel(window)
label.setText("Empty Text")
label.move(60,80)
 
button = QPushButton(window)
button.setText("Press me")
button.clicked.connect(display)
button.move(60,120)
 
window.show()
sys.exit(app.exec_())