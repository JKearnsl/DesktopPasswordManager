
from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main import MainModel
from src.views.main.ui.profileMenu import Ui_profileMenu


class ProfileView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_profileMenu()
        self.ui.setupUi(self)

        parent.ui.page_widget.addWidget(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass
