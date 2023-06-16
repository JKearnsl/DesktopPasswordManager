from src.controllers.main.settings import SettingsController
from src.controllers.main.resources import ResourcesController
from src.controllers.main.profile import ProfileController

from src.views.main.settings import SettingsView
from src.views.main.resources import ResourcesView
from src.views.main.profile import ProfileView

from src.views.main import MainView


class MainController:

    def __init__(self, model):
        self.model = model
        self.view = MainView(self, self.model)

        self.view.show()
        self.show_resources()

    def show_profile(self):
        self.view.ui.profile_menu_button.setChecked(True)
        if self.view.ui.page_widget.count() > 0:
            widget = self.view.ui.page_widget.currentWidget()
            if isinstance(widget, ProfileView):
                return

            if isinstance(widget, ResourcesView):
                self.view.ui.resources_menu_button.setChecked(False)

            if isinstance(widget, SettingsView):
                self.view.ui.settings_menu_button.setChecked(False)

            for i in range(self.view.ui.page_widget.count()):
                widget = self.view.ui.page_widget.widget(i)
                if isinstance(widget, ProfileView):
                    self.view.ui.page_widget.setCurrentWidget(widget)
                    return
        controller = ProfileController(self.model, self.view)

    def show_resources(self):
        self.view.ui.resources_menu_button.setChecked(True)
        if self.view.ui.page_widget.count() > 0:
            widget = self.view.ui.page_widget.currentWidget()

            if isinstance(widget, ProfileView):
                self.view.ui.profile_menu_button.setChecked(False)

            if isinstance(widget, SettingsView):
                self.view.ui.settings_menu_button.setChecked(False)

            for i in range(self.view.ui.page_widget.count()):
                widget = self.view.ui.page_widget.widget(i)
                if isinstance(widget, ResourcesView):
                    self.view.ui.page_widget.setCurrentWidget(widget)
                    return
        controller = ResourcesController(self.model, self.view)

    def show_settings(self):
        self.view.ui.settings_menu_button.setChecked(True)
        if self.view.ui.page_widget.count() > 0:
            widget = self.view.ui.page_widget.currentWidget()
            if isinstance(widget, ProfileView):
                self.view.ui.profile_menu_button.setChecked(False)

            if isinstance(widget, ResourcesView):
                self.view.ui.resources_menu_button.setChecked(False)

            for i in range(self.view.ui.page_widget.count()):
                widget = self.view.ui.page_widget.widget(i)
                if isinstance(widget, SettingsView):
                    self.view.ui.page_widget.setCurrentWidget(widget)
                    return
        controller = SettingsController(self.model, self.view)

    def close(self, event):
        self.model.save_session()
        event.accept()