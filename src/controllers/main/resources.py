from src.views.main.resources import ResourcesView


class ResourcesController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ResourcesView(self, self.model, parent)

        self.view.show()

    def resource_item_clicked(self, resource_id: int):
        print(f"pressed: {resource_id}")