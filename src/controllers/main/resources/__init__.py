from src.controllers.main.resources.data import DataController
from src.models.main.resource.data import DataModel
from src.views.main.resources import ResourcesView


class ResourcesController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ResourcesView(self, self.model, parent)

        self.view.show()
        self.view.model_loaded()

    def show_data(self, scope: dict):
        controller = DataController(DataModel(api=self.model.api_service, scope=scope), self.view)

    def search_resource(self, query: str):
        self.model.search_resources(query)

    def load_resource_list(self, page: int, per_page: int):
        self.model.load_resources(page=page, per_page=per_page)

    def add_resource(self, title: str):
        self.model.add_resource(title)

    def delete_resource(self, resource_id: str):
        self.model.delete_resource(resource_id)

    def update_resource(self, resource_id: str, title: str):
        self.model.update_resource(resource_id, title)
