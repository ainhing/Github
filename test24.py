from PyQt6.QtWidgets import QApplication, QMainWindow

from KTLT.py.d311224.ex24.ui.MainWindow24Ex import MainWindow24Ex

app=QApplication([])
myWindow= MainWindow24Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()
