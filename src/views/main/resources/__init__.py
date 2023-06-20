from typing import TypeVar

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.models.main.resource import ResourceModel
from src.views.main.resources.static_ui import Ui_resourcesMenu, ResourceItemWidget

ViewModel = TypeVar('ViewModel', bound=QtWidgets.QWidget)


class ResourcesView(QtWidgets.QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: ResourceModel, parent: ViewModel):
        super().__init__(parent)
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
        self.ui.add_resource_button.clicked.connect(self.show_ar_modal)
        self.ui.ar_button.clicked.connect(self.add_resource_clicked)
        self.ui.search_line.textChanged.connect(self.search_resource)
        self.ui.resource_list.verticalScrollBar().valueChanged.connect(self.resource_scroll_changed)

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
            item_widget.clicked.connect(self.resource_item_clicked)
            item.setSizeHint(QtCore.QSize(0, 50))
            self.ui.resource_list.addItem(item)
            self.ui.resource_list.setItemWidget(item, item_widget)

    def error_handler(self, error):
        QtWidgets.QMessageBox.critical(self, "Ошибка", error.content)

    def model_loaded(self):
        self.load_resource_list()

    def resource_item_clicked(self, data):
        resource_id = data[0]
        if self.current_resource:
            self.current_resource.unset_as_current()

        for i in range(self.ui.dp_layout.count()):
            if self.ui.dp_layout.itemAt(i).widget() != self.ui.dp_stub:
                self.ui.dp_layout.itemAt(i).widget().deleteLater()

        if self.current_resource == data[1]:
            self.current_resource = None
            self.ui.dp_stub.show()
            return

        data[1].set_as_current()
        self.current_resource = data[1]
        self.ui.dp_stub.hide()
        scope = {"resource_id": resource_id, "main_model": self.model.scope["main_model"]}
        self.controller.show_data(scope)

    def search_resource(self):
        if self.current_resource:
            self.current_resource.unset_as_current()
            self.current_resource = None
        query = self.ui.search_line.text()
        self.controller.search_resource(query)

    def load_resource_list(self):
        elems = self.ui.resource_list.count()
        per_page = (self.ui.resource_list.height() // 50) + 1
        page = (elems // per_page) + 1

        self.controller.load_resource_list(page, per_page=per_page)

    def add_resource_clicked(self):
        self.ui.ar_modal.close()
        title = self.ui.ar_title.text()
        self.controller.add_resource(title)
        self.ui.search_line.setText('')
        self.load_resource_list()

    def resource_scroll_changed(self, value: int):
        maximum = self.ui.resource_list.verticalScrollBar().maximum()
        if value == maximum:
            self.load_resource_list()

    def show_ar_modal(self):
        self.ui.ar_title.clear()
        self.ui.ar_modal.show()
