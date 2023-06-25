from typing import TypeVar

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from src.models.main.profile.change_password import CPModel
from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.profile.change_password.static_ui import UiCPModal

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class CPView(QtWidgets.QDialog, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: CPModel, parent: ViewModel):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiCPModal()
        self.ui.setup_ui(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass

    def error_handler(self, error):
        pass

    def model_loaded(self):
        pass
