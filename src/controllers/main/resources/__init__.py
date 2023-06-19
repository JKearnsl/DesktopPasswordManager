from src.controllers.main.resources.datum import DatumController
from src.models.main.resource.datum import DatumModel
from src.views.main.resources import ResourcesView


class ResourcesController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ResourcesView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()

    def show_datum(self, scope: dict):
        controller = DatumController(DatumModel(api=self.model.api_service, scope=scope), self.view)

    def search_resource(self, query: str):
        self.model.search_resources(query)

    def load_resource_list(self, page: int, per_page: int):
        self.model.load_resources(page=page, per_page=per_page)

    def add_resource(self, title: str):
        self.model.add_resource(title)
