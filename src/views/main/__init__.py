from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.MainWindow import Ui_MainWindow
from src.models.main import MainModel


class MainView(QtWidgets.QMainWindow, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("MainView")

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass
