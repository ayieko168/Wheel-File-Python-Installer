# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Wheel-File-Python-Installer/MainDesign.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(506, 187)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.WheelFileEntry = QtGui.QLineEdit(self.centralwidget)
        self.WheelFileEntry.setGeometry(QtCore.QRect(10, 20, 401, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei"))
        font.setPointSize(9)
        self.WheelFileEntry.setFont(font)
        self.WheelFileEntry.setObjectName(_fromUtf8("WheelFileEntry"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(420, 20, 75, 31))
        self.searchButton.setDefault(True)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.ExecuteButton = QtGui.QPushButton(self.centralwidget)
        self.ExecuteButton.setEnabled(False)
        self.ExecuteButton.setGeometry(QtCore.QRect(170, 70, 111, 41))
        self.ExecuteButton.setObjectName(_fromUtf8("ExecuteButton"))
        self.settingsButton = QtGui.QToolButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(480, 160, 25, 19))
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(20, 130, 471, 21))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.ExecuteButton.setText(_translate("MainWindow", "Execute!", None))
        self.settingsButton.setText(_translate("MainWindow", "...", None))
        self.statusLabel.setText(_translate("MainWindow", "Welcome...", None))

