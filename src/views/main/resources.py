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

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.add_resource_button.clicked.connect(self.show_add_resource_modal)
        self.ui.search_line.textChanged.connect(self.controller.search_resource)
        self.ui.resource_list.verticalScrollBar().valueChanged.connect(self.controller.resource_scroll_changed)

    def model_changed(self):
        if self.ui.resource_list.count() > len(self.model.loaded_resources):
            for i in range(self.ui.resource_list.count() - len(self.model.loaded_resources)):
                self.ui.resource_list.takeItem(self.ui.resource_list.count() - 1)

        for i, el in enumerate(self.model.loaded_resources):
            if item := self.ui.resource_list.item(i):
                item_widget: ResourceItemWidget = self.ui.resource_list.itemWidget(item)
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


class ResourceItemWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(str)

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

    def signal_change(self, *args, **kwargs):
        self.clicked.emit(self.id)
