from src.views.main.profile.change_password import CPView


class CPController:

    def __init__(self, model, parent):
        self.model = model
        self.view = CPView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()
