from src.views.main.resources import ResourcesView


class ResourcesController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ResourcesView(self, self.model, parent)

        self.view.show()
        self.load_resource_list()

    def add_password_clicked(self):
        resource_id = self.view.current_resource.id
        username = self.view.ui.nd_username_line.text()
        password = self.view.ui.nd_password_line.text()
        self.model.add_datum(resource_id, username, password)
        self.view.ui.nd_username_line.setText('')
        self.view.ui.nd_password_line.setText('')
        self.view.ui.add_password_modal.close()

    def datum_item_clicked(self, data):
        datum_id = data[0]
        username = data[1].username.text()
        password = data[1].enc_password
        self.view.show_password_modal(datum_id, username, password)

    def show_password_clicked(self):
        end_password = self.view.showed_password
        password = self.view.ui.sd_password_line.text()
        dec_password = self.model.get_datum_password(end_password, password)
        self.view.ui.nd_password_line.setText(dec_password)

    def resource_item_clicked(self, data):
        resource_id = data[0]
        if self.view.current_resource:
            self.view.current_resource.unset_as_current()

        if self.view.current_resource == data[1]:
            self.view.current_resource = None
            self.model.notify_observers()
            return
        data[1].set_as_current()
        self.view.current_resource = data[1]
        self.model.load_resource(resource_id)

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
