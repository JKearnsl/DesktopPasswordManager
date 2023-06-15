from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main import MainModel
from src.views.main.ui.resourceMenu import Ui_resourcesMenu


class ResourcesView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent):
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

        self.model_changed()

    def model_changed(self):
        for i in range(3):
            item = QtWidgets.QListWidgetItem(self.ui.resource_list)
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            item_widget = ResourceItemWidget(i, f"title #{i}")
            item_widget.clicked.connect(self.controller.resource_item_clicked)
            item.setSizeHint(QtCore.QSize(0, 50))
            print(item_widget.sizeHint())
            self.ui.resource_list.addItem(item)
            self.ui.resource_list.setItemWidget(item, item_widget)


class ResourceItemWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(int)

    def __init__(self, id: int, title: str, *args, **kwargs):
        super().__init__()

        self._id = id
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
        self.clicked.emit(self._id)
