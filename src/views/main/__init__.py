from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.ui.MainWindow import Ui_MainWindow
from src.models.main import MainModel


class MainView(QtWidgets.QMainWindow, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.profile_menu_button.clicked.connect(self.controller.show_profile)
        self.ui.resources_menu_button.clicked.connect(self.controller.show_resources)
        self.ui.settings_menu_button.clicked.connect(self.controller.show_settings)

    def model_changed(self):
        pass
