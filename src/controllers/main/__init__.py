from src.controllers.main.settings import SettingsController
from src.controllers.main.resources import ResourcesController
from src.controllers.main.profile import ProfileController
from src.views.main import MainView


class MainController:

    def __init__(self, model: 'MainModel'):
        self.model = model
        self.view = MainView(self, self.model)

        self.view.show()
        self.show_resources()

    def show_profile(self):
        if self.view.ui.page_widget.count() > 0:
            widget = self.view.ui.page_widget.currentWidget()
            self.view.ui.page_widget.removeWidget(widget)
            self.model.remove_observer(widget)
        controller = ProfileController(self.model, self.view)

    def show_resources(self):
        if self.view.ui.page_widget.count() > 0:
            widget = self.view.ui.page_widget.currentWidget()
            self.view.ui.page_widget.removeWidget(widget)
            self.model.remove_observer(widget)
        controller = ResourcesController(self.model, self.view)

    def show_settings(self):
        if self.view.ui.page_widget.count() > 0:
            widget = self.view.ui.page_widget.currentWidget()
            self.view.ui.page_widget.removeWidget(widget)
            self.model.remove_observer(widget)
        controller = SettingsController(self.model, self.view)
