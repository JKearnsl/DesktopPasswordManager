
from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main import MainModel
from src.views.main.settings.static_ui import Ui_settingsMenu


class SettingsView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_settingsMenu()
        self.ui.setupUi(self)

        parent.ui.page_widget.addWidget(self)
        parent.ui.page_widget.setCurrentWidget(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass

    def error_handler(self, error):
        pass