import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox,
                             QLineEdit, QPushButton)
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application's GUI """
        self.setMaximumSize(310, 130)
        self.setWindowTitle("JQLineEdit Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """ Create and arrange widgets in the main window """
        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(100, 10)
        catalogue_label.setFont(QFont('Arial', 18))

        search_label = QLabel("Search Results", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())