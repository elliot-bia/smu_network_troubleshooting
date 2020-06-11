# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 150, 180))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 200, 150, 180))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 400, 150, 180))
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 140, 181, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "南医大网络故障排查工具        @z"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
import source_rc
