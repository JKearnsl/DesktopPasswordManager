from typing import TypeVar

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from src.models.main.resource.datum import DatumModel
from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.resources.datum.static_ui import UiDatum, DatumItemWidget

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class DatumView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: DatumModel, parent: ViewModel):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiDatum()
        self.ui.setup_ui(self)

        parent.ui.dp_layout.addWidget(self.ui.datum)

        # Состояния отображений
        self.current_resource = parent.current_resource

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.add_datum_button.clicked.connect(self.show_add_datum_modal)
        self.ui.ad_button.clicked.connect(self.add_datum_clicked)
        self.ui.sd_decrypt_button.clicked.connect(self.decrypt_password_clicked)

    def model_changed(self):
        self.ui.datum_header_label.setText(self.current_resource.title.text())
        self.ui.datum_list.clear()
        for i, el in enumerate(self.model.data):
            item = QtWidgets.QListWidgetItem(self.ui.datum_list)
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            item_widget = DatumItemWidget(el["id"], username=el["username"], enc_password=el["password"])
            item_widget.clicked.connect(self.show_datum_modal)
            item.setSizeHint(QtCore.QSize(0, 50))
            self.ui.datum_list.addItem(item)
            self.ui.datum_list.setItemWidget(item, item_widget)

        self.ui.datum.show()

    def error_handler(self, error):
        print(error)

    def model_loaded(self):
        self.controller.load_data_list()

    def add_datum_clicked(self):
        resource_id = self.current_resource.id
        username = self.ui.ad_username_line.text()
        password = self.ui.ad_password_line.text()
        self.controller.add_datum(resource_id, username, password)
        self.ui.ad_modal.close()

    def show_add_datum_modal(self):
        self.ui.ad_username_line.clear()
        self.ui.ad_password_line.clear()
        self.ui.ad_modal.show()

    def show_datum_modal(self, data):
        widget = data
        self.ui.sd_modal.setWindowTitle(widget.id)
        self.ui.sd_username_line.setText(widget.username)
        self.ui.sd_enc_password = widget.enc_password
        self.ui.sd_user_password_line.clear()

        if not self.model.scope["resource_model"].private_key:
            self.ui.sd_password_line.setText('*' * 16)
            self.ui.decrypt_panel.show()
        else:
            self.ui.decrypt_panel.hide()
            self.ui.sd_password_line.setText(self.controller.decrypt_password(widget.enc_password))
        self.ui.sd_modal.show()

    def decrypt_password_clicked(self):
        enc_password = self.ui.sd_enc_password
        password = self.ui.sd_user_password_line.text()
        dec_password = self.controller.decrypt_password(enc_password, password)
        if not dec_password:
            self.ui.sd_password_line.setText('Неверный пароль')
        else:
            self.ui.sd_password_line.setText(dec_password)
            self.ui.decrypt_panel.hide()
