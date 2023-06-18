from src.views.main.resources import ResourcesView


class DataPanelController:

    def __init__(self, model, parent):
        self.model = model
        self.view = ResourcesView(self, self.model, parent)

        self.view.show()

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
