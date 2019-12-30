# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Wheel-File-Python-Installer/MainDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WheelFileEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.WheelFileEntry.setGeometry(QtCore.QRect(10, 20, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.WheelFileEntry.setFont(font)
        self.WheelFileEntry.setObjectName("WheelFileEntry")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(420, 20, 75, 31))
        self.searchButton.setDefault(True)
        self.searchButton.setObjectName("searchButton")
        self.ExecuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExecuteButton.setEnabled(False)
        self.ExecuteButton.setGeometry(QtCore.QRect(170, 70, 111, 41))
        self.ExecuteButton.setObjectName("ExecuteButton")
        self.settingsButton = QtWidgets.QToolButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(480, 160, 25, 19))
        self.settingsButton.setObjectName("settingsButton")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(20, 130, 471, 21))
        self.statusLabel.setObjectName("statusLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.ExecuteButton.setText(_translate("MainWindow", "Execute!"))
        self.settingsButton.setText(_translate("MainWindow", "..."))
        self.statusLabel.setText(_translate("MainWindow", "Welcome..."))
