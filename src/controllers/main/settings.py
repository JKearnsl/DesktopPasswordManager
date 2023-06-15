from src.views.main.settings import SettingsView


class SettingsController:

    def __init__(self, model, parent):
        self.model = model
        self.view = SettingsView(self, self.model, parent)

        self.view.show()

