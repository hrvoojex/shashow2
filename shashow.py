#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Learning PyQt5.

In this application, I created three classes,
added QGridLayout, connected key press to a
functions.

author: hrvooje
last edited: February 2017
"""

import sys
import crypt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QWidget,
    QApplication, QFrame, QGridLayout,QHBoxLayout, QMainWindow, QAction)


class About(QWidget):
    """A 'About' widget (page)"""
    def __init__(self, parent=None):
        super(About, self).__init__(parent)

        self.initui()


    def initui(self):
            """Initialize UI of a class About"""
            # add a label to write a file in it
            self.labelAbout = QLabel(self)

            # write a file in a label
            aboutfile = "About.txt"
            with open(aboutfile, "r") as f:
                data = f.read()
                self.labelAbout.setText(data)

            # add a widget self.labelAbout to a layout
            layout = QHBoxLayout()
            layout.addWidget(self.labelAbout)
            self.setLayout(layout)


class Main(QWidget):
    """A main widget (page) with labels and calculation button"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initui()


    def initui(self):
        """Initialize UI of main widget"""
        self.saltLabel = QLabel("Salt:")
        self.saltLine = QLineEdit()
        self.saltLine.setPlaceholderText("e.g. $6$xxxxxxxx")
        self.passwordLabel = QLabel("Password:")
        self.passwordLine = QLineEdit()
        self.hashLabel = QLabel("Hash:")
        self.hashSunkenLabel = QLabel()
        self.hashSunkenLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # enable selectable text to be able to copy it
        self.hashSunkenLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.resultButton = QPushButton("&Calculate", self)
        self.resultButton.sizeHint()
        self.resultButton.setMaximumSize(100, 50)

        # set layout
        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(self.passwordLabel, 0, 0)
        grid.addWidget(self.passwordLine, 0, 1)
        grid.addWidget(self.saltLabel, 1, 0)
        grid.addWidget(self.saltLine, 1, 1)
        grid.addWidget(self.resultButton, 2, 1)
        grid.addWidget(self.hashLabel, 3, 0)
        grid.addWidget(self.hashSunkenLabel, 3, 1)
        self.setLayout(grid)


class MyApp(QMainWindow):
    """Main application class"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initui()


    def initui(self):
        """Initialize UI of an application"""
        # main window size, title and icon
        self.setGeometry(300, 300, 800, 200)
        self.setWindowTitle("Password hash calculator | Linux")
        self.setWindowIcon(QIcon("shadow.png"))

        # create instances of your classes
        self.main = Main(self)
        self.about = About(self)

        # create central widget, create grid layout, add created instances
        #  of Main and About classes in it and set created widget as
        # central widget in MyApp instance
        centralWidget = QWidget()
        centralLayout = QGridLayout()
        centralLayout.addWidget(self.main, 0, 0)
        centralLayout.addWidget(self.about, 1, 0)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)

        # at start, show only main wigdet
        self.main.show()
        self.about.hide()

        # action for menu entrie "about"
        aboutAction = QAction(QIcon('exit.png'), "&About", self)
        aboutAction.setShortcut('Ctrl+B')
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.show_about)

        # action for menu entrie "main"
        mainAction = QAction(QIcon('exit.png'), "&Hash", self)
        mainAction.setShortcut('Ctrl+H')
        mainAction.setStatusTip('New')
        mainAction.triggered.connect(self.show_main)

        # menubar
        menu_bar = self.menuBar()
        fileMenu = menu_bar.addMenu("&File")
        fileMenu.addAction(mainAction)
        helpMenu = menu_bar.addMenu("&Help")
        helpMenu.addAction(aboutAction)

        # call logic function when button or return is pressed
        self.main.resultButton.clicked.connect(self.logic)
        # this method emits 'clicked' signal when 'Enter | Return' is pressed
        self.main.resultButton.setAutoDefault(True)
        self.main.passwordLine.returnPressed.connect(self.logic)
        self.main.saltLine.returnPressed.connect(self.logic)


    def show_main(self):
        """Action when 'Hash' menu is pressed"""
        self.about.hide()
        self.main.show()
        self.setWindowTitle("Password hash calculator | Linux")


    def show_about(self):
        """Action when 'about' menu is pressed"""
        self.main.hide()
        self.about.show()
        self.setWindowTitle("Password hash calculator | About | Linux")


    def logic(self):
        """Calculates hash from salt and password"""
        salt = self.main.saltLine.text()
        password = self.main.passwordLine.text()
        resulting_hash = crypt.crypt(password, salt)
        self.main.hashSunkenLabel.setText(resulting_hash)


    def keyPressEvent(self, e):
        """Action when return or escape is pressed"""
        if e.key() == Qt.Key_Return:
            self.logic()
        # self.close is MaApp close() which is QWidget's close()
        if e.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
