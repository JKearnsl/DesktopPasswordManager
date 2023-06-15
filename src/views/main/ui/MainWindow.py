from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""
            QMenuBar {
                background-color: transparent;
            }
            
            QMenuBar::item {
            color : black;
            margin-top:4px;
            spacing: 3px;
            padding: 1px 10px;
            background: transparent;
            border-radius: 4px;
            }
            
            QMenuBar::item:selected {
                color: rgb(247, 247, 247);
            background: #a8a8a8;
            }
            
            QMenuBar::item:pressed {
            background: #888888;
            }
            
            QMainWindow {
                background-color: rgb(220, 226, 218);
                border: none;
            }
        """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_layout.setObjectName("central_layout")
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        # Панель меню
        self.menu_panel = QtWidgets.QWidget()
        self.menu_panel.setObjectName("menu_panel")
        self.menu_panel.setContentsMargins(0, 0, 0, 0)
        self.menu_panel.setFixedWidth(64)
        self.menu_panel.setStyleSheet("""
            QWidget {
                background-color: #202e3b;
                border: none;
            }
        """)
        self.mp_layout = QtWidgets.QVBoxLayout(self.menu_panel)
        self.mp_layout.setObjectName("mp_layout")
        self.mp_layout.setContentsMargins(0, 0, 0, 0)

        self.resources_menu_button = QtWidgets.QPushButton(self.menu_panel)
        self.resources_menu_button.setObjectName("resources_menu_button")
        self.resources_menu_button.setText("R")
        self.resources_menu_button.setStyleSheet("""
            QPushButton {
                background-color: gray;
                border: none;
                color: rgb(0, 0, 0);
            };
        """)
        self.mp_layout.addWidget(self.resources_menu_button)

        self.profile_menu_button = QtWidgets.QPushButton(self.menu_panel)
        self.profile_menu_button.setObjectName("profile_menu_button")
        self.profile_menu_button.setText("P")
        self.profile_menu_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(220, 226, 218);
                border: none;
                color: rgb(0, 0, 0);
            };
        """)
        self.mp_layout.addWidget(self.profile_menu_button)

        self.settings_menu_button = QtWidgets.QPushButton(self.menu_panel)
        self.settings_menu_button.setObjectName("settings_menu_button")
        self.settings_menu_button.setText("S")
        self.settings_menu_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(220, 226, 218);
                border: none;
                color: rgb(0, 0, 0);
            };
        """)
        self.mp_layout.addWidget(self.settings_menu_button)
        self.central_layout.addWidget(self.menu_panel)

        # Поле страницы
        self.page_widget = QtWidgets.QStackedWidget()
        self.page_widget.setObjectName("page_widget")
        self.page_widget.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addWidget(self.page_widget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))

