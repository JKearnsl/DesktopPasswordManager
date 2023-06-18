from PyQt6 import QtWidgets

from src.models.enum.auth_state import AuthState
from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.login.static_ui import Ui_LoginWindow
from src.models.login import LoginModel


class LoginView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: LoginModel, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        if self.model.auth_state == AuthState.SIGNIN:
            self.signin_form()
        else:
            self.signup_form()

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.switchAuthStateLabel.mousePressEvent = self.controller.switch_auth_state
        self.ui.signin_button.clicked.connect(self.signin_clicked)
        self.ui.signup_button.clicked.connect(self.controller.signup)

    def model_changed(self):
        if self.model.auth_state == AuthState.SIGNIN:
            self.signin_form()
        else:
            self.signup_form()

        self.ui.authResponseLabel.clear()
        self.ui.authResponseLabel.hide()

    def error_handler(self, error):
        if error.type.MESSAGE:
            self.ui.authResponseLabel.show()
            self.ui.authResponseLabel.setText(error.content)

    def signin_clicked(self):
        login = self.ui.login_line_edit.text()
        password = self.ui.password_line_edit.text()
        self.controller.signin(login, password)

    def signup_clicked(self):
        login = self.ui.login_line_edit.text()
        password = self.ui.password_line_edit.text()
        repeat_password = self.ui.repeat_password_line_edit.text()
        self.controller.signup(login, password, repeat_password)

    def signin_form(self):
        self.ui.authTitleLabel.setText("Авторизация")
        self.ui.switchAuthStateLabel.setText("Регистрация")

        self.ui.password_line_edit.clear()
        self.ui.repeat_password_line_edit.clear()
        self.ui.signup_button.hide()
        self.ui.repeat_password_line_edit.hide()

        self.ui.signin_button.show()

    def signup_form(self):
        self.ui.authTitleLabel.setText("Регистрация")
        self.ui.switchAuthStateLabel.setText("Авторизация")

        self.ui.password_line_edit.clear()
        self.ui.repeat_password_line_edit.clear()
        self.ui.signin_button.hide()

        self.ui.repeat_password_line_edit.show()
        self.ui.signup_button.show()
