#!/usr/bin/env python3


import sys
import crypt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QWidget,
    QApplication, QFrame, QGridLayout, QMainWindow, QAction, qApp)


class MyApp(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initui()


    def initui(self):
        # main window size, title and icon
        self.setGeometry(300, 300, 800, 170)
        self.setWindowTitle("Password hash calculator | Linux")
        self.setWindowIcon(QIcon("shadow.png"))

        # central widget
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.widget.saltLabel = QLabel("Salt:")
        self.widget.saltLine = QLineEdit()
        self.widget.saltLine.setPlaceholderText("e.g. $6$xxxxxxxx")
        self.widget.passwordLabel = QLabel("Password:")
        self.widget.passwordLine = QLineEdit()
        self.widget.hashLabel = QLabel("Hash:")
        self.widget.hashSunkenLabel = QLabel()
        # self.hashSunkenLabel.setFrameStyle(QFrame.Box | QFrame.Sunken)
        self.widget.hashSunkenLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # enable selectable text to be able to copy it
        self.widget.hashSunkenLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.widget.resultButton = QPushButton("&Calculate", self)
        self.widget.resultButton.sizeHint()
        self.widget.resultButton.setMaximumSize(100, 50)

        aboutAction = QAction(QIcon('exit.png'), "&About", self)
        aboutAction.setShortcut('Ctrl+B')
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.show_about)

        # menubar
        menu_bar = self.menuBar()
        fileMenu = menu_bar.addMenu("&File")
        helpMenu = menu_bar.addMenu("&Help")
        helpMenu.addAction(aboutAction)

        # set layout
        grid = QGridLayout()
        grid.addWidget(self.widget.passwordLabel, 0, 0)
        grid.addWidget(self.widget.passwordLine, 0, 1)
        grid.addWidget(self.widget.saltLabel, 1, 0)
        grid.addWidget(self.widget.saltLine, 1, 1)
        grid.addWidget(self.widget.resultButton, 2, 1)
        grid.addWidget(self.widget.hashLabel, 3, 0)
        grid.addWidget(self.widget.hashSunkenLabel, 3, 1)
        self.widget.setLayout(grid)

        self.widget.resultButton.clicked.connect(self.logic)
        # this method emits 'clicked' signal when 'Enter' is pressed
        self.widget.resultButton.setAutoDefault(True)
        self.widget.passwordLine.returnPressed.connect(self.logic)
        self.widget.saltLine.returnPressed.connect(self.logic)


    def logic(self):
        """
        Calculates hash from salt and password
        """
        salt = self.widget.saltLine.text()
        password = self.widget.passwordLine.text()
        resulting_hash = crypt.crypt(password, salt)
        #if resulting_hash and salt and password:
        #    self.statusBar().showMessage("Ready")
        self.widget.hashSunkenLabel.setText(resulting_hash)


    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Return:
            self.logic()

        if e.key() == Qt.Key_Escape:
            self.close()


    def show_about(self):

        self.about = QWidget()
        #self.widget.hide()
        self.about.show()


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
