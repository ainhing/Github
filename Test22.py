from PyQt6.QtWidgets import QApplication, QMainWindow


from KTLT.py.d311224.ex22.ui.MainWindow22 import MainWindow22

app=QApplication([])
myWindow= MainWindow22()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()