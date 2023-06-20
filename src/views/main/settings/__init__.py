from typing import TypeVar

from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main import MainModel
from src.views.main.settings.static_ui import UiSettingsMenu

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class SettingsView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent: ViewModel):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiSettingsMenu()
        self.ui.setup_ui(self)

        parent.ui.page_widget.addWidget(self)
        parent.ui.page_widget.setCurrentWidget(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass

    def error_handler(self, error):
        pass
