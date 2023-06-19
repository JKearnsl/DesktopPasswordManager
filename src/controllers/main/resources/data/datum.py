from src.views.main.resources.data.datum import DatumView


class DatumController:

    def __init__(self, model, parent):
        self.model = model
        self.view = DatumView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()

    def decrypt_password(self, user_password: str = None):
        self.model.decrypt_datum_password(user_password)
