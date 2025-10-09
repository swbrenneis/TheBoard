import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from registration import NewUserDialog

class LoginWindow(QWidget):

    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application's GUI"""
        self.setFixedSize(360, 220)
        self.setWindowTitle("3.1 - Login GUI")
        self.setUpWindow()
        self.show()

    def setUpWindow(self):
        """ Create and arrange widgets in the main window """
        self.login_is_successful = False

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)

        username_label = QLabel("Username", self)
        username_label.move(20, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.resize(250, 24)
        self.username_edit.move(90, 50)

        password_label = QLabel("Password", self)
        password_label.move(20, 86)

        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)

        # Create QCheckbox for displaying password
        self.show_password_cb = QCheckBox(
            "Show Password", self
        )
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(
            self.displayPasswordIfChecked)

        # Create QPushButton for signing in
        login_button = QPushButton("Login", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        # Create sign up QLabel and QPushButton
        not_member_label = QLabel("Sign up", self)
        not_member_label.move(20, 186)

        sign_up_button = QPushButton("Sign up", self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.createNewUser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())