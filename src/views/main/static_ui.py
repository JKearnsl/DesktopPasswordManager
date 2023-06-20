from PyQt6 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        main_window.setStyleSheet("""
            QMainWindow {
                background-color: rgb(220, 226, 218);
                border: none;
            }
        """)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.central_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_layout.setObjectName("central_layout")
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setProperty("spacing", 0)
        main_window.setCentralWidget(self.centralwidget)

        # Панель меню
        self.menu_panel = QtWidgets.QWidget()
        self.menu_panel.setObjectName("menu_panel")
        self.menu_panel.setContentsMargins(0, 0, 0, 0)
        self.menu_panel.setFixedWidth(96)
        self.menu_panel.setStyleSheet("""
            QWidget {
                background-color: #293a4c;
                border: none;
            }
        """)
        self.mp_layout = QtWidgets.QVBoxLayout(self.menu_panel)
        self.mp_layout.setObjectName("mp_layout")
        self.mp_layout.setContentsMargins(0, 0, 0, 0)
        self.mp_layout.setProperty("spacing", 0)

        self.profile_menu_button = QtWidgets.QPushButton(self.menu_panel)
        self.profile_menu_button.setObjectName("profile_menu_button")
        self.profile_menu_button.setIcon(QtGui.QIcon("assets:menu_icon/profile.png"))
        self.profile_menu_button.setIconSize(QtCore.QSize(64, 64))
        self.profile_menu_button.setCheckable(True)
        self.profile_menu_button.setStyleSheet("""
            QPushButton {
                padding: 5px;
                border: none;
            }

            QPushButton:hover {
                background-color: #304459;
            }

            QPushButton:pressed {
                background-color: #253545;
            }

            QPushButton:checked {
                background-color: black;
            }

        """)
        self.mp_layout.addWidget(self.profile_menu_button)

        self.resources_menu_button = QtWidgets.QPushButton(self.menu_panel)
        self.resources_menu_button.setObjectName("resources_menu_button")
        self.resources_menu_button.setIcon(QtGui.QIcon("assets:menu_icon/resources.png"))
        self.resources_menu_button.setIconSize(QtCore.QSize(64, 64))
        self.resources_menu_button.setCheckable(True)
        self.resources_menu_button.setStyleSheet("""
            QPushButton {
                padding: 5px;
                border: none;
            }

            QPushButton:hover {
                background-color: #304459;
            }

            QPushButton:pressed {
                background-color: #253545;
            }

            QPushButton:checked {
                background-color: black;
            }
        """)
        self.mp_layout.addWidget(self.resources_menu_button)
        self.mp_layout.addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        )

        self.settings_menu_button = QtWidgets.QPushButton(self.menu_panel)
        self.settings_menu_button.setObjectName("settings_menu_button")
        self.settings_menu_button.setIconSize(QtCore.QSize(64, 64))
        self.settings_menu_button.setIcon(QtGui.QIcon("assets:menu_icon/settings.png"))
        self.settings_menu_button.setCheckable(True)
        self.settings_menu_button.setStyleSheet("""
            QPushButton {
                padding: 5px;
                border: none;
            }

            QPushButton:hover {
                background-color: #304459;
            }

            QPushButton:pressed {
                background-color: #253545;
            }

            QPushButton:checked {
                background-color: black;
            }
        """)
        self.mp_layout.addWidget(self.settings_menu_button)
        self.central_layout.addWidget(self.menu_panel)
        self.mp_layout.addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        # Поле страницы
        self.page_widget = QtWidgets.QStackedWidget()
        self.page_widget.setObjectName("page_widget")
        self.page_widget.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addWidget(self.page_widget)

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindowTitle", "Password Manager"))

