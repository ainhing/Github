# Form implementation generated from reading ui file 'D:\Kỹ thuật lập trình\KTLT\py\d311224\exercise21\ui\MainWindow24.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 649)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 80, 581, 201))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditN = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditN.setGeometry(QtCore.QRect(170, 40, 311, 22))
        self.lineEditN.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.lineEditN.setObjectName("lineEditN")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditK = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditK.setGeometry(QtCore.QRect(170, 90, 311, 22))
        self.lineEditK.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.lineEditK.setObjectName("lineEditK")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 531, 31))
        self.label.setObjectName("label")
        self.pushButtonexecute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonexecute.setGeometry(QtCore.QRect(310, 300, 151, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Nhi/OneDrive/Hình ảnh/Ảnh chụp màn hình/Screenshot 2024-12-12 093633.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonexecute.setIcon(icon)
        self.pushButtonexecute.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonexecute.setObjectName("pushButtonexecute")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 360, 581, 201))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 55, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditA = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditA.setGeometry(QtCore.QRect(180, 40, 311, 22))
        self.lineEditA.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEditA.setObjectName("lineEditA")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 90, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEditC = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditC.setGeometry(QtCore.QRect(180, 90, 311, 22))
        self.lineEditC.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEditC.setObjectName("lineEditC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "InPut N and K"))
        self.label_2.setText(_translate("MainWindow", "Input N"))
        self.label_3.setText(_translate("MainWindow", "Input K"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0055ff;\">Combinations and permutations</span></p></body></html>"))
        self.pushButtonexecute.setText(_translate("MainWindow", "Execute"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Results"))
        self.label_4.setText(_translate("MainWindow", "A="))
        self.label_5.setText(_translate("MainWindow", "C="))
