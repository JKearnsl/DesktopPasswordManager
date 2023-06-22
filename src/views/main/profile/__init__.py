from typing import TypeVar

from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main import MainModel
from src.views.main.profile.static_ui import UiProfileMenu

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class ProfileView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent: ViewModel):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiProfileMenu()
        self.ui.setup_ui(self)

        parent.ui.page_widget.addWidget(self)
        parent.ui.page_widget.setCurrentWidget(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.logout_button.clicked.connect(self.logout_clicked)

    def model_changed(self):
        pass

    def error_handler(self, error):
        pass

    def logout_clicked(self):
        box = QtWidgets.QMessageBox(self)
        box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        box.setWindowTitle("Выход")
        box.setText("Вы действительно хотите выйти?")
        box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        box.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        box.setWindowIcon(self.windowIcon())
        box.setStyleSheet("""
        QLabel {
            font-size: 14px;
        }
        
        QPushButton {
            min-width: 100px;
            min-height: 30px;
            font-size: 14px;
            border-radius: 5px;
            background-color: white;
            border: 1px solid #d0d0d0;
        }
        
        QPushButton:hover {
            background-color: #e0e0e0;
        }
        
        QPushButton:pressed {
            background-color: #d0d0d0;
        }
        """)
        if box.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            self.controller.logout()
