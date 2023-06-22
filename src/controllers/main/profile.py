from src.controllers import login
from src.models.login import LoginModel
from src.views.main.profile import ProfileView


class ProfileController:

    def __init__(self, model, parent):
        self.model = model
        self.main_model = parent
        self.view = ProfileView(self, self.model, parent)

        self.view.show()

    def logout(self):
        self.model.logout()
        self.main_model.close()
        controller = login.LoginController(LoginModel())

