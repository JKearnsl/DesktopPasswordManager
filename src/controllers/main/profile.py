from src.views.main.profile import ProfileView


class ProfileController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ProfileView(self, self.model, parent)

        self.view.show()

