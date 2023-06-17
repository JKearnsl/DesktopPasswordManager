from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsDropShadowEffect

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.resource import ResourceModel
from src.views.main.ui.resourceMenu import Ui_resourcesMenu


class ResourcesView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: ResourceModel, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_resourcesMenu()
        self.ui.setupUi(self)

        parent.ui.page_widget.addWidget(self)
        parent.ui.page_widget.setCurrentWidget(self)

        # Состояния отображений
        self.current_resource = None

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.add_resource_button.clicked.connect(self.show_add_resource_modal)
        self.ui.datum_add_button.clicked.connect(self.show_add_password_modal)
        self.ui.search_line.textChanged.connect(self.controller.search_resource)
        self.ui.resource_list.verticalScrollBar().valueChanged.connect(self.controller.resource_scroll_changed)

    def model_changed(self):
        if self.ui.resource_list.count() > len(self.model.loaded_resources):
            for i in range(self.ui.resource_list.count() - len(self.model.loaded_resources)):
                self.ui.resource_list.takeItem(self.ui.resource_list.count() - 1)

        for i, el in enumerate(self.model.loaded_resources):
            if item := self.ui.resource_list.item(i):
                item_widget = self.ui.resource_list.itemWidget(item)
                item_widget.id = el["id"]
                item_widget.title.setText(el["title"])
                continue

            item = QtWidgets.QListWidgetItem(self.ui.resource_list)
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            item_widget = ResourceItemWidget(el["id"], title=el["title"])
            item_widget.clicked.connect(self.controller.resource_item_clicked)
            item.setSizeHint(QtCore.QSize(0, 50))
            self.ui.resource_list.addItem(item)
            self.ui.resource_list.setItemWidget(item, item_widget)

        self.ui.datum_list.clear()
        if self.current_resource:
            self.ui.dp_stub.hide()
            self.ui.dp_layout.addWidget(self.ui.datum)
            self.ui.datum_header_label.setText(self.current_resource.title.text())

            for i, el in enumerate(self.model.data):
                item = QtWidgets.QListWidgetItem(self.ui.datum_list)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                item_widget = DatumItemWidget(el["id"], username=el["username"])
                item_widget.clicked.connect(self.controller.datum_item_clicked)
                item.setSizeHint(QtCore.QSize(0, 50))
                self.ui.datum_list.addItem(item)
                self.ui.datum_list.setItemWidget(item, item_widget)

            self.ui.datum.show()
        else:
            self.ui.datum.hide()
            self.ui.datum_header_label.clear()
            self.ui.dp_stub.show()

    def show_add_resource_modal(self):
        self.ui.add_resource_modal = QtWidgets.QDialog(self)
        self.ui.add_resource_modal.setModal(True)
        self.ui.add_resource_modal.setMinimumSize(QtCore.QSize(400, 200))
        self.ui.add_resource_modal.setWindowTitle("Добавить ресурс")
        self.ui.add_resource_modal.setStyleSheet("""
            QDialog {
                background-color: white;
            }
        """)
        layout = QtWidgets.QFormLayout(self.ui.add_resource_modal)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setProperty("spacing", 30)

        text_1 = QtWidgets.QLabel("Title:")
        text_1.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
        """)

        self.ui.new_resource_title = QtWidgets.QLineEdit()
        self.ui.new_resource_title.setObjectName("new_resource_title")
        self.ui.new_resource_title.setMaxLength(128)
        self.ui.new_resource_title.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        layout.addRow(text_1, self.ui.new_resource_title)

        # Кнопка
        button = QtWidgets.QPushButton("Добавить")
        button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
            
            QPushButton:hover {
                background-color: #f1f1f1;
            }
        """)
        button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        button.clicked.connect(self.controller.add_resource_clicked)
        layout.addRow(button)

        self.ui.add_resource_modal.show()

    def show_add_password_modal(self):
        self.ui.add_password_modal = QtWidgets.QDialog(self)
        self.ui.add_password_modal.setModal(True)
        self.ui.add_password_modal.setMinimumSize(QtCore.QSize(500, 200))
        self.ui.add_password_modal.setWindowTitle("Добавить пароль")
        self.ui.add_password_modal.setStyleSheet(""" 
            QDialog { background-color: white; } 
            QLineEdit {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
            
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }

            QPushButton:hover {
                background-color: #f1f1f1;
            }
        """)
        layout = QtWidgets.QFormLayout(self.ui.add_password_modal)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setProperty("spacing", 30)

        # Username
        self.ui.nd_username_line = QtWidgets.QLineEdit()
        self.ui.nd_username_line.setMaxLength(128)
        layout.addRow(QtWidgets.QLabel("Username:"), self.ui.nd_username_line)

        # Password
        self.ui.nd_password_line = QtWidgets.QLineEdit()
        self.ui.nd_password_line.setMaxLength(64)
        self.ui.nd_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addRow(QtWidgets.QLabel("Password:"), self.ui.nd_password_line)

        # Кнопка
        button = QtWidgets.QPushButton("Добавить")
        button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        button.clicked.connect(self.controller.add_password_clicked)
        layout.addRow(button)

        self.ui.add_password_modal.show()

    def show_password_modal(self, datum_id: str, username: str):
        self.ui.show_password_modal = QtWidgets.QDialog(self)
        self.ui.show_password_modal.setModal(True)
        self.ui.show_password_modal.setMinimumSize(QtCore.QSize(500, 200))
        self.ui.show_password_modal.setWindowTitle("Пароль")
        self.ui.show_password_modal.setStyleSheet(""" 
            QDialog { background-color: white; } 
            QLineEdit {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }

            QLabel {
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }

            QPushButton:hover {
                background-color: #f1f1f1;
            }
        """)
        layout = QtWidgets.QFormLayout(self.ui.show_password_modal)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setProperty("spacing", 30)

        # Username
        self.ui.nd_username_label = QtWidgets.QLineEdit(username)
        self.ui.nd_username_label.setReadOnly(True)
        layout.addRow(QtWidgets.QLabel("Username:"), self.ui.nd_username_label)

        # Password
        self.ui.nd_password_label = QtWidgets.QLineEdit("*" * 16)
        self.ui.nd_password_label.setReadOnly(True)
        layout.addRow(QtWidgets.QLabel("Password:"), self.ui.nd_password_label)

        layout.addRow(QtWidgets.QLabel("Для расшифровки введите пароль:"))

        # User Password
        self.ui.sd_password_line = QtWidgets.QLineEdit()
        self.ui.sd_password_line.setMaxLength(64)
        self.ui.sd_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addRow(QtWidgets.QLabel("Password:"), self.ui.sd_password_line)

        # Кнопка
        button = QtWidgets.QPushButton("Расшифровать")
        button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        button.clicked.connect(self.controller.show_password_clicked)
        layout.addRow(button)

        self.ui.show_password_modal.show()


class ResourceItemWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(tuple)

    def __init__(self, id: str, title: str, *args, **kwargs):
        super().__init__()

        self.id = id
        self.title = QtWidgets.QLabel(title)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.title)

        self.setLayout(layout)
        self.mouseReleaseEvent = self.signal_change

        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            
            QWidget:hover {
                background-color: #f1f1f1;
            }
        """)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 10px;
            }
        """)
        self.title.setWordWrap(False)
        self.setFixedHeight(50)

    def set_as_current(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f1f1f1;
            }
        """)

    def unset_as_current(self):
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            
            QWidget:hover {
                background-color: #f1f1f1;
            }
        """)

    def signal_change(self, *args, **kwargs):
        self.clicked.emit((self.id, self))


class DatumItemWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(tuple)

    def __init__(self, id: str, username: str, *args, **kwargs):
        super().__init__()

        self.id = id
        self.username = QtWidgets.QLabel(username)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.username)

        self.setLayout(layout)
        self.mouseReleaseEvent = self.signal_change

        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border-bottom: 1px solid #ccc;
                border-radius: 5px;
            }

            QWidget:hover {
                background-color: #f1f1f1;
            }
        """)
        self.username.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: medium;
                padding: 10px;
                padding-left: 20px;
            }
        """)
        self.username.setWordWrap(False)
        self.setFixedHeight(50)

    def signal_change(self, *args, **kwargs):
        self.clicked.emit((self.id, self))
