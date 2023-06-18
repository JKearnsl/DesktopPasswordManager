from src.controllers.main import MainController
from src.models.main import MainModel
from src.views.login import LoginView


class LoginController:

    def __init__(self, model: 'LoginModel'):
        self.model = model
        self.view = LoginView(self, self.model)

        self.view.show()

    def switch_auth_state(self, event=None):
        self.model.switch_auth_state()

    def signin(self, login: str, password: str):
        if self.model.signin(login, password):
            self.view.hide()
            controller = MainController(MainModel(self.model.api_service))

    def signup(self, login: str, password: str, repeat_password: str):
        if self.model.signup(login, password, repeat_password):
            self.switch_auth_state()
