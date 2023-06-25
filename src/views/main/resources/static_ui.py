from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class UiResourcesMenu(object):
    def setup_ui(self, resource_menu):
        resource_menu.setObjectName("resource_menu")
        self.central_layout = QtWidgets.QHBoxLayout(resource_menu)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setObjectName("central_layout")
        self.central_layout.setProperty("spacing", 0)

        # Разделитель
        self.separator = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.separator.setObjectName("separator")
        self.separator.setContentsMargins(0, 0, 0, 0)
        self.separator.setProperty("spacing", 0)
        self.separator.setStyleSheet("""
            QSplitter::handle:vertical {
                width: 0px;
            }

        """)

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

        self.rp_layout = QtWidgets.QVBoxLayout(self.resource_panel)
        self.rp_layout.setObjectName("rp_layout")
        self.rp_layout.setContentsMargins(0, 0, 0, 0)
        self.rp_layout.setProperty("spacing", 0)
        self.resource_panel.setLayout(self.rp_layout)

        # Шапка панели ресурсов
        self.rp_header = QtWidgets.QWidget()
        self.rp_header.setObjectName("rp_header")
        self.rp_header.setContentsMargins(0, 0, 0, 0)
        self.rp_header.setFixedHeight(60)
        self.rp_header.setStyleSheet("""
            QWidget {
                background-color: white;
                border-right: 1px solid #d1d1d1;
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
                border: 1px solid #d1d1d1;
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
        self.resource_list.verticalScrollBar().setSingleStep(5)
        self.resource_list.setStyleSheet("""
            QListWidget {
                border-right: 1px solid #d1d1d1;
                border-top: 1px solid #d1d1d1;
                font-size: 16px;
            }

            QListWidget:item:selected {
                color: white;
            }

            QScrollBar:vertical { width: 5px; }


            QScrollBar::add-line:vertical {
                  border: none;
                  background: none;
            }

            QScrollBar::sub-line:vertical {
                  border: none;
                  background: none;
            }

            QScrollBar::handle:vertical {
                    background: #d1d1d1;
                    border-radius: 2px;
            }

            QScrollBar::handle:vertical:hover {
                    background: #c1c1c1;
            }

            QScrollBar::handle:vertical:pressed {
                    background: #b1b1b1;
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
        self.dp_layout.setProperty("spacing", 0)
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

        # modal
        self.ar_modal = QtWidgets.QDialog(resource_menu)
        self.ar_modal.setModal(True)
        self.ar_modal.setMinimumSize(QtCore.QSize(400, 200))
        self.ar_modal.setWindowTitle("Добавить ресурс")
        self.ar_modal.setStyleSheet("""
            QDialog {
                background-color: white;
            }
        """)
        layout = QtWidgets.QFormLayout(self.ar_modal)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setProperty("spacing", 30)

        text_1 = QtWidgets.QLabel("Title:")
        text_1.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
        """)

        self.ar_title = QtWidgets.QLineEdit()
        self.ar_title.setMaxLength(128)
        self.ar_title.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        layout.addRow(text_1, self.ar_title)

        # Кнопка
        self.ar_button = QtWidgets.QPushButton("Добавить")
        self.ar_button.setStyleSheet("""
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
        self.ar_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))

        layout.addRow(self.ar_button)

        self.separator.addWidget(self.datum_panel)
        self.central_layout.addWidget(self.separator)

        self.translate_ui(resource_menu)
        QtCore.QMetaObject.connectSlotsByName(resource_menu)

    def translate_ui(self, resource_menu):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))


class ResourceItemWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(tuple)

    def __init__(self, _id: str, title: str, *args, **kwargs):
        super().__init__()

        self.id = _id
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
