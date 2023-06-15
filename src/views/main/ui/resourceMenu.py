from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class Ui_resourcesMenu(object):
    def setupUi(self, settingsMenu):
        settingsMenu.setObjectName("settingsMenu")
        self.central_layout = QtWidgets.QHBoxLayout(settingsMenu)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setObjectName("central_layout")
        self.central_layout.setProperty("spacing", 0)

        # Разделитель
        self.separator = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.separator.setObjectName("separator")
        self.separator.setContentsMargins(0, 0, 0, 0)

        # Панель ресурсов
        self.resource_panel = QtWidgets.QWidget()
        self.resource_panel.setObjectName("resource_panel")
        self.resource_panel.setContentsMargins(0, 0, 0, 0)
        self.resource_panel.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        rp_size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred
        )
        rp_size_policy.setHorizontalStretch(1)
        self.resource_panel.setSizePolicy(rp_size_policy)
        self.resource_panel.setMinimumWidth(300)

        self.rp_layout = QtWidgets.QVBoxLayout(self.resource_panel)
        self.rp_layout.setObjectName("rp_layout")
        self.rp_layout.setContentsMargins(0, 0, 0, 0)
        self.rp_layout.setProperty("spacing", 0)
        self.resource_panel.setLayout(self.rp_layout)

        # Шапка панели ресурсов
        self.rp_header = QtWidgets.QWidget()
        self.rp_header.setObjectName("rp_header")
        self.rp_header.setContentsMargins(0, 0, 0, 0)
        self.rp_header.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)
        self.rp_header_layout = QtWidgets.QHBoxLayout(self.rp_header)
        self.rp_header_layout.setObjectName("rp_header_layout")
        self.rp_header_layout.setContentsMargins(0, 0, 0, 0)
        self.rp_header_layout.setProperty("spacing", 0)

        self.search_line = QtWidgets.QLineEdit()
        self.search_line.setObjectName("search_line")
        self.search_line.setStyleSheet("""
            QLineEdit {
                background-color: #f1f1f1;
                border: 1px solid #d1d1d1;
                border-radius: 5px;
                padding: 5px;
                margin: 15px;
                font-size: 16px;
            }
        """)
        self.search_line.setPlaceholderText("Поиск")
        self.rp_header_layout.addWidget(self.search_line)

        self.add_resource_button = QtWidgets.QPushButton()
        self.add_resource_button.setObjectName("add_resource_button")
        self.add_resource_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 15px;
            }
            
            QPushButton:hover {
                background-color: #f1f1f1;
            }
            
            QPushButton:pressed {
                background-color: #e1e1e1;
            }
            
        """)
        self.add_resource_button.setIcon(QtGui.QIcon("assets:/menu_icon/plus.png"))
        self.add_resource_button.setIconSize(QtCore.QSize(20, 20))
        self.add_resource_button.setFixedSize(32, 32)
        self.add_resource_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        self.rp_header_layout.addWidget(self.add_resource_button)
        self.rp_header_layout.addItem(
            QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        self.rp_layout.addWidget(self.rp_header)

        # Список элементов ресурса
        self.resource_list = QtWidgets.QListWidget()
        self.resource_list.setObjectName("resource_list")
        self.resource_list.setStyleSheet("""
            QListWidget {
                border-top: 1px solid #d1d1d1;
                font-size: 16px;
            }
        """)

        self.rp_layout.addWidget(self.resource_list)

        self.separator.addWidget(self.resource_panel)

        # Панель данных
        self.datum_panel = QtWidgets.QWidget()
        self.datum_panel.setObjectName("datum_panel")
        self.datum_panel.setContentsMargins(0, 0, 0, 0)
        self.datum_panel.setStyleSheet("""
            QWidget {
                
            }
        """)
        dp_size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred
        )
        dp_size_policy.setHorizontalStretch(2)
        self.datum_panel.setSizePolicy(dp_size_policy)
        self.dp_layout = QtWidgets.QVBoxLayout(self.datum_panel)
        self.dp_layout.setObjectName("dp_layout")
        self.dp_layout.setContentsMargins(0, 0, 0, 0)
        self.datum_panel.setLayout(self.dp_layout)

        self.dp_stub = QtWidgets.QWidget()
        self.dp_stub.setObjectName("dp_stub")
        self.dp_stub_layout = QtWidgets.QVBoxLayout(self.dp_stub)
        self.dp_stub_layout.setObjectName("dp_stub_layout")
        self.dp_stub_layout.setContentsMargins(0, 0, 0, 0)
        self.dp_stub_layout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        self.dp_stub_label = QtWidgets.QLabel()
        self.dp_stub_label.setObjectName("dp_stub_label")
        self.dp_stub_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
                margin: 20px;
                padding: 2px;
                border-radius: 10px;
                background-color: rgba(100, 100, 100, 100);
            }
        """)
        self.dp_stub_label.setText("Выберите ресурс")
        self.dp_stub_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.dp_stub_layout.addWidget(self.dp_stub_label)
        self.dp_stub_layout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        self.dp_layout.addWidget(self.dp_stub)

        self.separator.addWidget(self.datum_panel)
        self.central_layout.addWidget(self.separator)

        self.retranslateUi(settingsMenu)
        QtCore.QMetaObject.connectSlotsByName(settingsMenu)

    def retranslateUi(self, settingsMenu):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))
