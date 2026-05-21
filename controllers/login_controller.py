from PyQt6 import QtWidgets, uic
import sys
sys.path.append('.')       

class LoginController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_login.clicked.connect(self.handle_login)
    def handle_login(self):
        username = self.window.txt_user.text()
        password = self.window.txt_pass.text()
        if username == "admin" and password =="123":
            self.window.login_successful.emit()
        else:
            QtWidgets.QMessageBox.warning(self.window, None, "Error")