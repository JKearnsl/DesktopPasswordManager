from typing import TypeVar

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from src.models.main.resource.data.datum import DatumModel
from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.resources.data.datum.static_ui import UiDatumItemModal

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class DatumView(QtWidgets.QDialog, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: DatumModel, parent: ViewModel):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiDatumItemModal()
        self.ui.setup_ui(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.decrypt_button.clicked.connect(self.decrypt_password_clicked)

    def model_changed(self):
        if self.ui.error_label.isVisible():
            self.ui.error_label.hide()

        if self.model.dec_password is not None:
            self.ui.password_line.setText(self.model.dec_password)

            if self.ui.decrypt_panel.isVisible():
                self.ui.decrypt_panel.hide()

    def error_handler(self, error):
        if error.type.MESSAGE:
            self.ui.error_label.show()
            self.ui.error_label.setText(error.content)

    def model_loaded(self):
        self.setWindowTitle(self.model.id)
        self.ui.username_line.setText(self.model.username)

        if not self.model.scope["resource_model"].private_key:
            self.ui.decrypt_panel.show()
        else:
            self.ui.decrypt_panel.hide()
            self.controller.decrypt_password()

    def decrypt_password_clicked(self):
        password = self.ui.user_password_line.text()
        self.controller.decrypt_password(password)
