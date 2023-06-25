from typing import TypeVar

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main.profile import ProfileModel
from src.views.main.profile.static_ui import UiProfileMenu

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class ProfileView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: ProfileModel, parent: ViewModel):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiProfileMenu()
        self.ui.setup_ui(self)

        parent.ui.page_widget.addWidget(self)
        parent.ui.page_widget.setCurrentWidget(self)

        self.ui.change_password_button.setEnabled(False)
        self.ui.change_keys_button.setEnabled(False)

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.logout_button.clicked.connect(self.logout_clicked)
        self.ui.save_button.clicked.connect(self.save_clicked)
        self.ui.change_password_button.clicked.connect(self.change_password_clicked)

    def model_changed(self):
        current_user_name = self.model.current_user().get("username")
        self.ui.username_input.setText(current_user_name)

    def error_handler(self, error):
        # Todo: error label
        pass

    def model_loaded(self):
        self.model_changed()

    def save_clicked(self):
        current_user_name = self.model.current_user().get("username")
        new_user_name = self.ui.username_input.text().strip()
        if current_user_name != new_user_name:
            box = QtWidgets.QDialog(self)
            box.setWindowIcon(self.windowIcon())
            box.setWindowTitle("Изменение имени пользователя")
            box.setModal(True)
            box.setFixedSize(300, 200)
            box.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                }
                
                QLineEdit {
                    min-width: 100px;
                    min-height: 30px;
                    font-size: 14px;
                    border-radius: 5px;
                    border: 1px solid #d0d0d0;
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
                    background-color: #f1f1f1;
                }
                
                QPushButton:pressed {
                    background-color: #e1e1e1;
                }
            """)
            box.setLayout(QtWidgets.QVBoxLayout())
            box.layout().setContentsMargins(10, 10, 10, 10)
            box.layout().setSpacing(10)

            label = QtWidgets.QLabel(box)
            label.setText("Для изменения имени пользователя необходимо ввести пароль, чтобы обновить хеш на сервере.")
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            box.layout().addWidget(label)

            password_input = QtWidgets.QLineEdit(box)
            password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            password_input.setPlaceholderText("Пароль")
            box.layout().addWidget(password_input)

            buttons = QtWidgets.QWidget(box)
            buttons.setLayout(QtWidgets.QHBoxLayout())
            buttons.layout().setContentsMargins(0, 0, 0, 0)
            buttons.layout().setSpacing(10)
            box.layout().addWidget(buttons)

            cancel_button = QtWidgets.QPushButton(buttons)
            cancel_button.setText("Отмена")
            cancel_button.clicked.connect(box.close)
            buttons.layout().addWidget(cancel_button)

            save_button = QtWidgets.QPushButton(buttons)
            save_button.setText("Сохранить")
            save_button.clicked.connect(box.accept)
            buttons.layout().addWidget(save_button)

            if box.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                user_password = password_input.text().strip()
                self.controller.change_username(new_user_name, user_password)

    def change_password_clicked(self):
        self.controller.show_change_password()

    def change_keys_clicked(self):
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
