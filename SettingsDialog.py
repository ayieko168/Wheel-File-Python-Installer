# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Wheel-File-Python-Installer/SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(551, 156)
        settingsDialog.setMaximumSize(QtCore.QSize(551, 156))
        self.editCheck = QtWidgets.QGroupBox(settingsDialog)
        self.editCheck.setGeometry(QtCore.QRect(10, 10, 541, 80))
        self.editCheck.setCheckable(True)
        self.editCheck.setChecked(False)
        self.editCheck.setObjectName("editCheck")
        self.commandEntry = QtWidgets.QLineEdit(self.editCheck)
        self.commandEntry.setGeometry(QtCore.QRect(10, 20, 521, 20))
        self.commandEntry.setObjectName("commandEntry")
        self.setButton = QtWidgets.QPushButton(self.editCheck)
        self.setButton.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.setButton.setObjectName("setButton")
        self.resetButton = QtWidgets.QPushButton(self.editCheck)
        self.resetButton.setGeometry(QtCore.QRect(350, 50, 75, 23))
        self.resetButton.setObjectName("resetButton")

        self.retranslateUi(settingsDialog)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Dialog"))
        self.editCheck.setTitle(_translate("settingsDialog", "Edit Command"))
        self.setButton.setText(_translate("settingsDialog", "Set"))
        self.resetButton.setText(_translate("settingsDialog", "Reset"))
