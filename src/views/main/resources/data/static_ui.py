from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class UiDatum:
    def setup_ui(self, ui_datum):
        ui_datum.setObjectName("ui_datum")
        self.central_layout = QtWidgets.QHBoxLayout(ui_datum)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setObjectName("central_layout")
        self.central_layout.setProperty("spacing", 0)

        self.datum = QtWidgets.QWidget()
        self.datum.setObjectName("data")
        self.datum_layout = QtWidgets.QVBoxLayout(self.datum)
        self.datum_layout.setObjectName("datum_layout")
        self.datum_layout.setContentsMargins(0, 0, 0, 0)
        self.datum_layout.setProperty("spacing", 0)

        # header
        self.datum_header = QtWidgets.QWidget()
        self.datum_header.setObjectName("datum_header")
        self.datum_header.setStyleSheet("""
                    QWidget {
                        background-color: white;
                    }
                """)
        self.datum_header.setFixedHeight(60)
        self.datum_header_layout = QtWidgets.QHBoxLayout(self.datum_header)
        self.datum_header_layout.setObjectName("datum_header_layout")
        self.datum_header_layout.setContentsMargins(0, 0, 0, 0)
        self.datum_header_layout.addItem(
            QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )
        self.datum_header_label = QtWidgets.QLabel()
        self.datum_header_label.setObjectName("datum_header_label")
        self.datum_header_label.setStyleSheet("""
                    QLabel {
                        font-size: 18px;
                        font-weight: bold;
                        color: black;

                    }
                """)
        self.datum_header_label.setText("Title")
        self.datum_header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.datum_header_layout.addWidget(self.datum_header_label)
        self.datum_layout.addWidget(self.datum_header)

        # list
        self.datum_list = QtWidgets.QListWidget()
        self.datum_list.setObjectName("datum_list")
        self.datum_list.setStyleSheet("""
            QListWidget {
                background-color: transparent;
                font-size: 16px;
                margin: 10px;
            }

            QListWidget:item {
                border-bottom: 1px solid #ccc;
                border-radius: 5px;
                background-color: white;
            }

            QListWidget:item:selected {
                color: white;
            }
        """)
        self.datum_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.datum_layout.addWidget(self.datum_list)

        # footer
        self.datum_footer = QtWidgets.QWidget()
        self.datum_footer.setObjectName("datum_footer")
        self.datum_footer.setStyleSheet("""
                    QWidget {
                        background-color: white;
                        border-top: 1px solid #d1d1d1;
                    }
                """)
        self.datum_footer.setFixedHeight(50)
        self.datum_footer_layout = QtWidgets.QHBoxLayout(self.datum_footer)
        self.datum_footer_layout.setObjectName("datum_footer_layout")
        self.datum_footer_layout.setContentsMargins(0, 0, 0, 0)
        self.datum_footer_layout.addItem(
            QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )
        self.add_datum_button = QtWidgets.QPushButton()
        self.add_datum_button.setObjectName("add_datum_button")
        self.add_datum_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                color: black;
                border-radius: 4px;
                border: 1px solid #d1d1d1;
            }

            QPushButton:hover {
                background-color: #f1f1f1;
            }

            QPushButton:pressed {
                background-color: #e1e1e1;
            }
        """)
        self.add_datum_button.setText("+")
        self.add_datum_button.setMinimumWidth(100)
        self.add_datum_button.setMaximumWidth(200)
        self.add_datum_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        self.datum_footer_layout.addWidget(self.add_datum_button)
        self.datum_layout.addWidget(self.datum_footer)
        self.datum_footer_layout.addItem(
            QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        # Modal: add data
        self.ad_modal = QtWidgets.QDialog(ui_datum)
        self.ad_modal.setModal(True)
        self.ad_modal.setMinimumSize(QtCore.QSize(500, 200))
        self.ad_modal.setWindowTitle("Добавить пароль")
        self.ad_modal.setStyleSheet(""" 
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
        layout = QtWidgets.QFormLayout(self.ad_modal)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setProperty("spacing", 30)

        # Username
        self.ad_username_line = QtWidgets.QLineEdit()
        self.ad_username_line.setMaxLength(128)
        layout.addRow(QtWidgets.QLabel("Username:"), self.ad_username_line)

        # Password
        passwd_layout = QtWidgets.QHBoxLayout()
        passwd_layout.setContentsMargins(0, 0, 0, 0)
        passwd_layout.setSpacing(0)
        self.ad_password_line = QtWidgets.QLineEdit()
        self.ad_password_line.setMaxLength(64)
        self.ad_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        passwd_layout.addWidget(self.ad_password_line)

        # r_panel
        r_panel = QtWidgets.QWidget(self.ad_modal)
        r_panel.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        r_panel_layout = QtWidgets.QHBoxLayout(r_panel)
        r_panel_layout.setContentsMargins(4, 4, 4, 4)
        r_panel_layout.setSpacing(0)

        self.show_password_button = QtWidgets.QCheckBox()
        self.show_password_button.setIconSize(QtCore.QSize(30, 30))
        self.show_password_button.setFixedSize(QtCore.QSize(38, 32))
        self.show_password_button.setChecked(False)
        self.show_password_button.setIcon(QtGui.QIcon("assets:/datum_icon/hide_pass.png"))
        self.show_password_button.setStyleSheet("""
            QCheckBox {
                border: none;
            }
        
            QCheckBox::indicator {
                background-color:transparent;
                selection-background-color:transparent;
                color:transparent;
                selection-color:transparent;
                width: 0px;
                height: 0px;
                padding: 0px;
                margin: 0px
            }
        """)
        self.show_password_button.clicked.connect(
            lambda is_checked:
                self.show_password_button.setIcon(QtGui.QIcon("assets:/datum_icon/show_pass.png")) if is_checked else
                self.show_password_button.setIcon(QtGui.QIcon("assets:/datum_icon/hide_pass.png"))
        )
        r_panel_layout.addWidget(self.show_password_button)

        self.gen_password_button = QtWidgets.QPushButton()
        self.gen_password_button.setIconSize(QtCore.QSize(30, 30))
        self.gen_password_button.setFixedSize(QtCore.QSize(32, 32))
        self.gen_password_button.setIcon(QtGui.QIcon("assets:/datum_icon/gen_pass.png"))
        self.gen_password_button.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
                border: 1px;
                margin-left: 2px;
            }
        
        """)
        r_panel_layout.addWidget(self.gen_password_button)


        passwd_layout.addWidget(r_panel)
        layout.addRow(QtWidgets.QLabel("Password:"), passwd_layout)

        # Кнопка
        self.ad_button = QtWidgets.QPushButton("Добавить")
        self.ad_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        layout.addRow(self.ad_button)

        self.retranslateUi(ui_datum)
        QtCore.QMetaObject.connectSlotsByName(ui_datum)

    def retranslateUi(self, ui_datum):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))


class DatumItemWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(QtWidgets.QWidget)

    def __init__(self, _id: str, username: str, enc_password: str, *args, **kwargs):
        super().__init__()

        self._id = _id
        self._enc_password = enc_password
        self._username = QtWidgets.QLabel(username)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._username)

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
        self._username.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: medium;
                padding: 10px;
                padding-left: 20px;
            }
        """)
        self._username.setWordWrap(False)
        self.setFixedHeight(50)

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username.text()

    @property
    def enc_password(self):
        return self._enc_password

    def signal_change(self, *args, **kwargs):
        self.clicked.emit(self)
