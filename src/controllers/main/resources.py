from src.views.main.resources import ResourcesView


class ResourcesController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ResourcesView(self, self.model, parent)

        self.view.show()
        self.load_resource_list()

    def resource_item_clicked(self, resource_id: str):
        print(f"pressed: {resource_id}")

    def search_resource(self):
        query = self.view.ui.search_line.text()
        self.model.search_resources(query)

    def load_resource_list(self):
        elems = self.view.ui.resource_list.count()
        per_page = (self.view.ui.resource_list.height() // 50) + 1

        self.model.load_resources(page=(elems // per_page) + 1, per_page=per_page)

    def add_resource_clicked(self):
        self.view.ui.add_resource_modal.close()
        self.model.add_resource(self.view.ui.new_resource_title.text())
        self.view.ui.search_line.setText('')
        self.load_resource_list()

    def resource_scroll_changed(self, value: int):
        maximum = self.view.ui.resource_list.verticalScrollBar().maximum()
        if value == maximum:
            self.load_resource_list()
