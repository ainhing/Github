from PyQt6.QtWidgets import QApplication, QMainWindow


from KTLT.py.d311224.exercise21.ui.MainWindow21Ex import MainWindow21Ex

app=QApplication([])
myWindow= MainWindow21Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()