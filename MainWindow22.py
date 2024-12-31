from KTLT.py.d311224.ex22.ui.ex22 import  Ui_MainWindow
from KTLT.py.d311224.ex22.libs.math22 import combination

class MainWindow22(Ui_MainWindow):

    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalansSlot()

    def show(self):
        self.MainWindow.show()
    def setupSignalansSlot(self):
        self.pushButtonclrar.clicked.connect(self.clear)
        self.pushButtonexecute.clicked.connect(self.execute)
    def execute(self):
       try:
        n = int(self.lineEditgroupbox.text())
        m = int(self.lineEdittakeout.text())
        d = int(self.lineEditDamaged.text())
        if m>n or d > n or m<=0 or d<0:
          self.lineEditOutcome.setText("invalid)")
        tu = combination(d,1) * combination(n-d,m-1)
        mau = combination(n,m)
        P = tu / mau
        self.lineEditOutcome.setText(str(P))
       except:
        self.lineEditOutcome.setText("invalid")
    def clear(self):
        self.lineEditDamaged.clear()
        self.lineEditgroupbox.clear()
        self.lineEdittakeout.clear()
        self.lineEditOutcome.clear()