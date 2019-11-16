# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Wheel-File-Python-Installer/SettingsDialog.ui'
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

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(551, 156)
        settingsDialog.setMaximumSize(QtCore.QSize(551, 156))
        self.editCheck = QtGui.QGroupBox(settingsDialog)
        self.editCheck.setGeometry(QtCore.QRect(10, 10, 541, 80))
        self.editCheck.setCheckable(True)
        self.editCheck.setChecked(False)
        self.editCheck.setObjectName(_fromUtf8("editCheck"))
        self.commandEntry = QtGui.QLineEdit(self.editCheck)
        self.commandEntry.setGeometry(QtCore.QRect(10, 20, 521, 20))
        self.commandEntry.setObjectName(_fromUtf8("commandEntry"))
        self.setButton = QtGui.QPushButton(self.editCheck)
        self.setButton.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.setButton.setObjectName(_fromUtf8("setButton"))
        self.resetButton = QtGui.QPushButton(self.editCheck)
        self.resetButton.setGeometry(QtCore.QRect(350, 50, 75, 23))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))

        self.retranslateUi(settingsDialog)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Dialog", None))
        self.editCheck.setTitle(_translate("settingsDialog", "Edit Command", None))
        self.setButton.setText(_translate("settingsDialog", "Set", None))
        self.resetButton.setText(_translate("settingsDialog", "Reset", None))

