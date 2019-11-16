from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MainDesign import *
from SettingsDialog import *
import os, threading

whlPath = ""
command = "python -m pip install \"{}\"".format(whlPath)

class SettingsDialog(QDialog):

    def __init__(self, cmd):

        global command, whlPath

        super().__init__()
        self.SettingsUi = Ui_settingsDialog()
        self.SettingsUi.setupUi(self)
        
        cmd = cmd.replace("\"\"", "<path_to_whl_file>")
        self.SettingsUi.commandEntry.setText(cmd)

        # CONNECTIONS
        self.SettingsUi.editCheck.clicked.connect(self.editCheckCMD)
        self.SettingsUi.setButton.clicked.connect(self.setCommand)
        self.SettingsUi.resetButton.clicked.connect(self.resetCommand)


    def editCheckCMD(self):

        global command, whlPath

        if self.SettingsUi.editCheck.isChecked():
            pass
        else:
            command = "python -m pip install \"{}\"".format(whlPath)
            print(command)

    def setCommand(self):

        global command, whlPath

        newCommand = self.SettingsUi.commandEntry.text()
        newCommand = newCommand.replace("<path_to_whl_file>", "\"{}\"".format(whlPath))
        print(newCommand)
        command = newCommand

        self.close()


    def resetCommand(self):

        global command, whlPath

        command = "python -m pip install \"{}\"".format(whlPath)
        print(command)
        
        self.close()


class App(QMainWindow):

    def __init__(self):

        global command, whlPath

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # CONNECTIONS
        self.ui.searchButton.clicked.connect(self.searchWhlFile)
        self.ui.ExecuteButton.clicked.connect(self.execute)
        self.ui.settingsButton.clicked.connect(self.settingsCMD)
        self.ui.WheelFileEntry.textChanged.connect(self.whlEntryTextChangeCMD)

    def searchWhlFile(self):

        global whlPath

        print("search for wheel file to install")

        filePath = QFileDialog.getOpenFileNameAndFilter(filter="Wheel Files (*.whl)")[0]
        fileName = filePath.split("/")[-1]
        self.ui.WheelFileEntry.setText(fileName)

        whlPath = filePath
        self.ui.ExecuteButton.setEnabled(True)

    def execute(self):
        global command, whlPath

        print("Execute install command")
        self.ui.statusLabel.setText("Executing install command...")

        windowsCommand = "python -m pip install \"{}\" && pause".format(whlPath)
        command = windowsCommand
        self.ui.statusLabel.setText("command ran is .. \"{}\"".format(command))
        
        # self.ui.statusLabel.setText("Thread started Successfully.")
        threading.Thread(target= lambda: os.system(command)).start()

    def settingsCMD(self):
        global command, whlPath

        print("Open settings Dialog")

        settingsobject = SettingsDialog(command)
        settingsobject.show()
        settingsobject.exec_()

    def whlEntryTextChangeCMD(self):

        print("change")
        if (".whl" in self.ui.WheelFileEntry.text()) and (os.path.exists(self.ui.WheelFileEntry.text())):
            whlPath = self.ui.WheelFileEntry.text()
            print("path set")

if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()