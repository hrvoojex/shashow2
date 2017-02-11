#!/usr/bin/env python3


import sys
import crypt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton,QWidget,
    QApplication, QFrame, QGridLayout)


class MyApp(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initui()


    def initui(self):
        # main window size, title and icon
        self.setGeometry(300, 300, 800, 170)
        self.setWindowTitle("Password hash calculator | Linux")
        self.setWindowIcon(QIcon("shadow.png"))

        self.saltLabel = QLabel("Salt:")
        self.saltLine = QLineEdit()
        self.saltLine.setPlaceholderText("e.g. $6$xxxxxxxx")
        self.passwordLabel = QLabel("Password:")
        self.passwordLine = QLineEdit()
        self.hashLabel = QLabel("Hash:")
        self.hashSunkenLabel = QLabel()
        # self.hashSunkenLabel.setFrameStyle(QFrame.Box | QFrame.Sunken)
        self.hashSunkenLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # enable selectable text to be able to copy it
        self.hashSunkenLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.resultButton = QPushButton("&Calculate", self)
        self.resultButton.setMaximumSize(100, 50)

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
        # this method emits 'clicked' signal when 'Enter' is pressed
        self.resultButton.setAutoDefault(True)
        self.passwordLine.returnPressed.connect(self.logic)
        self.saltLine.returnPressed.connect(self.logic)


    def logic(self):
        """
        Calculates hash from salt and password
        """
        salt = self.saltLine.text()
        password = self.passwordLine.text()
        resulting_hash = crypt.crypt(password, salt)
        self.hashSunkenLabel.setText(resulting_hash)


    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Return:
            self.logic()


    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
