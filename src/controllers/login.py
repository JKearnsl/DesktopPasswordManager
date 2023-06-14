from src.views.login import LoginView


class LoginController:

    def __init__(self, model: 'LoginModel'):
        self.model = model
        self.view = LoginView(self, self.model)

        self.view.show()

    def switch_auth_state(self, event):
        self.model.switch_auth_state()

    def signin(self):
        login = self.view.ui.login_line_edit.text()
        password = self.view.ui.password_line_edit.text()
        self.model.signin(login, password)

    def signup(self):
        login = self.view.ui.login_line_edit.text()
        password = self.view.ui.password_line_edit.text()
        repeat_password = self.view.ui.repeat_password_line_edit.text()
        self.model.signup(login, password, repeat_password)