from PyQt6 import QtWidgets

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.profile import ProfileView
from src.views.main.resources import ResourcesView
from src.views.main.settings import SettingsView
from src.views.main.static_ui import Ui_MainWindow
from src.models.main import MainModel


class MainView(QtWidgets.QMainWindow, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.profile_menu_button.clicked.connect(self.show_profile)
        self.ui.resources_menu_button.clicked.connect(self.show_resources)
        self.ui.settings_menu_button.clicked.connect(self.show_settings)
        self.closeEvent = self.controller.close

    def model_changed(self):
        pass

    def error_handler(self, error):
        pass

    def model_loaded(self):
        self.show_resources()


    def switch_page(self, widget_type: type[QtWidgets.QWidget]):
        if self.ui.page_widget.count() > 0:
            widget = self.ui.page_widget.currentWidget()
            if isinstance(widget, widget_type):
                return

            if isinstance(widget, ProfileView):
                self.ui.profile_menu_button.setChecked(False)

            if isinstance(widget, ResourcesView):
                self.ui.resources_menu_button.setChecked(False)

            if isinstance(widget, SettingsView):
                self.ui.settings_menu_button.setChecked(False)

        if widget_type == ProfileView:
            self.ui.profile_menu_button.setChecked(True)
        elif widget_type == ResourcesView:
            self.ui.resources_menu_button.setChecked(True)
        elif widget_type == SettingsView:
            self.ui.settings_menu_button.setChecked(True)

    def show_profile(self):
        self.switch_page(ProfileView)
        for i in range(self.ui.page_widget.count()):
            widget = self.ui.page_widget.widget(i)
            if isinstance(widget, ProfileView):
                self.ui.page_widget.setCurrentWidget(widget)
                return
        self.controller.show_profile()

    def show_resources(self):
        self.switch_page(ResourcesView)
        for i in range(self.ui.page_widget.count()):
            widget = self.ui.page_widget.widget(i)
            if isinstance(widget, ResourcesView):
                self.ui.page_widget.setCurrentWidget(widget)
                return
        self.controller.show_resources()

    def show_settings(self):
        self.switch_page(SettingsView)
        for i in range(self.ui.page_widget.count()):
            widget = self.ui.page_widget.widget(i)
            if isinstance(widget, SettingsView):
                self.ui.page_widget.setCurrentWidget(widget)
                return
        self.controller.show_settings()
