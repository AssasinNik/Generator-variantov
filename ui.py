# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 744)
        MainWindow.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 271))
        self.frame.setStyleSheet("background-color: rgb(78, 236, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, -10, 381, 101))
        self.label.setStyleSheet("font: 87 18pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 201, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-pLA8idXrMUrYrqm-removebg-preview.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 640, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 236, 236);\n"
"    border-radius: 30; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52, 158, 158);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(50, 300, 380, 60))
        self.type.setStyleSheet("QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"    border-radius: 30;\n"
"    border-color: rgb(78, 236, 236);\n"
"    font: 87 12pt \"Arial Black\";\n"
"    color: rgb(124, 124, 124);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(124, 124, 124);    \n"
"  background-color: rgb(49, 49, 49);\n"
"  padding: 10px;\n"
"  selection-background-color: rgb(49, 49, 49);\n"
"}")
        self.type.setObjectName("type")
        self.uroven = QtWidgets.QComboBox(self.centralwidget)
        self.uroven.setGeometry(QtCore.QRect(50, 410, 380, 60))
        self.uroven.setStyleSheet("QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}\n"
"QComboBox {\n"
"    border: 2px solid;\n"
"    border-radius: 30;\n"
"    border-color: rgb(78, 236, 236);\n"
"    font: 87 12pt \"Arial Black\";\n"
"    color: rgb(124, 124, 124);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(124, 124, 124);    \n"
"  background-color: rgb(49, 49, 49);\n"
"  padding: 10px;\n"
"  selection-background-color: rgb(49, 49, 49);\n"
"}")
        self.uroven.setObjectName("uroven")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 520, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2px solid;\n"
"border-radius: 30;\n"
"border-color: rgb(78, 236, 236);\n"
"background-color: rgb(49, 49, 49);\n"
"color: rgb(124, 124, 124);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "?????????????????? ??????????????????"))
        self.pushButton.setText(_translate("MainWindow", "?????????????? ??????????????"))
