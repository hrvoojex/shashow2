#!/usr/bin/env python3


import sys
import crypt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QLabel, QLineEdit, QPushButton,
    QWidget, QApplication, QSystemTrayIcon, QFrame, QGridLayout)



class MyApp(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.saltLabel = QLabel("Salt:")
        self.saltLine = QLineEdit()
        self.saltLine.setPlaceholderText("e.g. $6$xxxxxxxx")
        self.passwordLabel = QLabel("Password:")
        self.passwordLine = QLineEdit()
        self.hashLabel = QLabel("Hash:")
        self.hashSunkenLabel = QLabel()
        # widget.hashSunkenLabel.setFrameStyle(QFrame.Box | QFrame.Sunken)
        self.hashSunkenLabel.setFrameShadow(QFrame.Sunken)
        self.resultButton = QPushButton("&Calculate", self)
        self.resultButton.setMaximumSize(100, 50)

        self.initui()

    def initui(self):
        # main window size, title and icon
        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle("Password hash calculator | Linux")

        # set layout
        grid = QGridLayout()
        grid.addWidget(self.passwordLabel, 0, 0)
        grid.addWidget(self.passwordLine, 0, 1)
        grid.addWidget(self.saltLabel, 1, 0)
        grid.addWidget(self.saltLine, 1, 1)
        grid.addWidget(self.resultButton, 2, 1)
        grid.addWidget(self.hashLabel, 3, 0)
        grid.addWidget(self.hashSunkenLabel, 3, 1)
        self.setLayout(grid)

        self.resultButton.clicked.connect(self.logic)


    def logic(self):
        """
        Calculates hash from salt and password
        """
        salt = self.saltLine.text()
        password = self.passwordLine.text()
        resulting_hash = crypt.crypt(password, salt)
        self.hashSunkenLabel.setText(resulting_hash)
        # sender = self.sender()
        # print(sender)
        # print(dir(MyApp))


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
