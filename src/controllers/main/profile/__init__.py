from src.controllers import login
from src.controllers.main.profile.change_password import CPController
from src.models.login import LoginModel
from src.models.main.profile import ProfileModel
from src.models.main.profile.change_password import CPModel
from src.views.main.profile import ProfileView


class ProfileController:

    def __init__(self, model: ProfileModel, parent):
        self.model = model
        self.main_model = parent
        self.view = ProfileView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()

    def logout(self):
        self.model.logout()
        self.main_model.close()
        controller = login.LoginController(LoginModel())

    def change_username(self, new_username: str, password: str):
        self.model.change_username(new_username, password)

    def show_change_password(self):
        controller = CPController(CPModel(api=self.model.api_service), self.view)

    def show_change_keys(self):
        pass