from PyQt6.QtWidgets import QApplication, QMainWindow

from KTLT.py.d311224.ex23.ui.MainWindow23 import MainWindow23

app=QApplication([])
myWindow= MainWindow23()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()