#!/Usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import crypt
from linuxShadowShow import Ui_TabWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt



class MyApp(QTabWidget, Ui_TabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Shadow Hash Calculator")

        # If you click pushButton or press enter in QLineEdit
        self.pushButton.clicked.connect(self.calculation)
        self.pushButton.setAutoDefault(True)
        self.lineEdit.returnPressed.connect(self.calculation)
        self.lineEdit_2.returnPressed.connect(self.calculation)

        # Show a picture in a label
        self.pixmap = QPixmap('hash.png')
        self.label_4.setPixmap(self.pixmap)

        # Dispaly a text in a laybel and wrap it
        self.label_5.setText(
            "If you look in '<i>/etc/shadow</i>' file, this is how "
            "hashed password looks like. The <i>salt</i> part has a number in"
            "it. $6$ is for sha512crypt sheme and the password is the key. ")

        self.label_5.setWordWrap(True)

        # Add some local changes to widgets in gui file
        self.label_3.setText("")
        self.addTab(self.tab, "Hash calculator")
        self.addTab(self.tab_2, "About")
        self.lineEdit.setPlaceholderText("$6$mySalt")
        self.lineEdit_2.setPlaceholderText("myPassword")

    def calculation(self):
        """Calculates hash from salt and password"""
        salt = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.hash = crypt.crypt(password, salt)

        self.label_3.setText(self.hash)

    def keyPressEvent(self, e):
        """Action when return or escape is pressed"""
        if e.key() == Qt.Key_Return:
            self.calculation()
        # self.close is MaApp close() which is QWidget's close()
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        """Ask for closing confirmation"""
        reply = QMessageBox.question(
            self, 'Message', "Quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
