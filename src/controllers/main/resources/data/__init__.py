from src.controllers.main.resources.data.datum import DatumController
from src.models.main.resource.data.datum import DatumModel
from src.views.main.resources.data import DataView


class DataController:

    def __init__(self, model, parent):
        self.model = model
        self.view = DataView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()

    def load_data_list(self):
        self.model.load_data_list()

    def add_datum(self, resource_id: str, username: str, password: str):
        self.model.add_datum(resource_id, username, password)
        self.load_data_list()

    def show_datum(self, scope: dict):
        controller = DatumController(DatumModel(api=self.model.api_service, scope=scope), self.view)

    def delete_datum(self, datum_id: str):
        self.model.delete_datum(datum_id)

    def get_hard_password(self):
        return self.model.gen_hard_password()
