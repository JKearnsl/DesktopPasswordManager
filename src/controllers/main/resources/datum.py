from src.views.main.resources import ResourcesView
from src.views.main.resources.datum import DatumView


class DatumController:

    def __init__(self, model, parent):
        self.model = model
        self.view = DatumView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()

    def load_data_list(self):
        self.model.load_data_list()

    def add_datum(self, resource_id: str, username: str, password: str):
        self.model.add_datum(resource_id, username, password)
        self.load_data_list()

    def decrypt_password(self, end_password: str, password: str = None):
        return self.model.get_datum_password(end_password, password)
