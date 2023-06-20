from src.controllers.main.settings import SettingsController
from src.controllers.main.resources import ResourcesController
from src.controllers.main.profile import ProfileController
from src.models.main.profile import ProfileModel
from src.models.main.resource import ResourceModel

from src.views.main import MainView


class MainController:

    def __init__(self, model):
        self.model = model
        self.view = MainView(self, self.model)

        self.view.show()
        self.view.model_loaded()

    def show_settings(self):
        controller = SettingsController(self.model, self.view)

    def show_resources(self, scope: dict[str]):
        controller = ResourcesController(ResourceModel(self.model.api_service, scope=scope), self.view)

    def show_profile(self):
        controller = ProfileController(ProfileModel(self.model.api_service), self.view)

    def close(self):
        self.model.save_session()
