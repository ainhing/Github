import random
from KTLT.py.d311224.ex24.ui.MainWindow24 import Ui_MainWindow


class MainWindow24Ex(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalansSlot()

        self.machine_coin = 100
        self.player_coin = 100
    def show(self):
        self.MainWindow.show()
    def setupSignalansSlot(self):
        self.pushButtonrandom.clicked.connect(self.process)
        self.pushButtonnewgame.clicked.connect(self.new)
    def process(self):
        if self.player_coin < 30:
            self.lineEditplayer.setText('dont enough coin')
        self.machine_coin +=30
        self.player_coin -=30
        number = [random.randint(0, 8), random.randint(0, 9), random.randint(0, 10)]


        for i, num in enumerate(number):
            self.label1.setText(str(number[0]))
            self.label2.setText(str(number[1]))
            self.label3.setText(str(number[2]))

        reward1 = reward2 = reward3 = 0
        if number[0] ==7:
            reward1= 100 + 0.5*self.machine_coin
            self.player_coin += reward1
            self.machine_coin -= reward1
        if number[1]==7:
            reward2 = 30 + 0.5*self.machine_coin
            self.player_coin += reward2
            self.machine_coin -= reward2
        if number[2]==7:
            reward3=10
            self.player_coin += reward3
        self.lineEditmachine.setText(f"{self.machine_coin}")
        self.lineEditplayer.setText(f'{self.player_coin}')
    def new(self):
        self.player_coin = 100
        self.machine_coin = 100
        self.lineEditplayer.setText(f"{self.player_coin}")
        self.lineEditmachine.setText(f'{self.machine_coin}')
        self.label1.setText('0')
        self.label2.setText('0')
        self.label3.setText('0')
