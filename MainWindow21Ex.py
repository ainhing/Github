from KTLT.py.d311224.exercise21.libs.function import A,C
from KTLT.py.d311224.exercise21.ui.MainWindow21 import Ui_MainWindow


class MainWindow21Ex(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalansSlot()

    def show(self):
        self.MainWindow.show()
    def setupSignalansSlot(self):
        self.pushButtonexecute.clicked.connect(self.processreusult)
    def processreusult(self):
        n = int(self.lineEditN.text())
        k = int(self.lineEditK.text())
        a = A(n,k)
        c = C(n,k)
        self.lineEditA.setText(str(a))
        self.lineEditC.setText(f"{c}")

