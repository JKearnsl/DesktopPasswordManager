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
        self.datum.setObjectName("datum")
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

        # Modal: add datum
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
        self.ad_password_line = QtWidgets.QLineEdit()
        self.ad_password_line.setMaxLength(64)
        self.ad_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addRow(QtWidgets.QLabel("Password:"), self.ad_password_line)

        # Кнопка
        self.ad_button = QtWidgets.QPushButton("Добавить")
        self.ad_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        layout.addRow(self.ad_button)

        # Modal: show datum
        self.sd_modal = QtWidgets.QDialog(ui_datum)
        self.sd_modal.setModal(True)
        self.sd_modal.setMinimumSize(QtCore.QSize(500, 200))
        self.sd_modal.setWindowTitle("Пароль")
        self.sd_modal.setStyleSheet(""" 
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
        layout = QtWidgets.QFormLayout(self.sd_modal)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setProperty("spacing", 30)

        # Title
        self.sd_datum_id = QtWidgets.QLabel()
        self.sd_datum_id.setObjectName("sd_datum_id")
        self.sd_datum_id.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: black;
            }
        """)
        self.sd_datum_id.setText("Просмотр данных")
        self.sd_datum_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addRow(self.sd_datum_id)

        # Username
        self.sd_username_line = QtWidgets.QLineEdit()
        self.sd_username_line.setReadOnly(True)
        layout.addRow(QtWidgets.QLabel("Username:"), self.sd_username_line)

        # Password
        self.sd_password_line = QtWidgets.QLineEdit("*" * 16)
        self.sd_password_line.setReadOnly(True)
        layout.addRow(QtWidgets.QLabel("Password:"), self.sd_password_line)

        # Decrypt panel
        self.sd_enc_password = None
        self.decrypt_panel = QtWidgets.QWidget()
        self.decrypt_panel.setObjectName("decrypt_panel")
        self.decrypt_panel.setStyleSheet("""
            QWidget#decrypt_panel {
                background-color: #f1f1f1;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        self.decrypt_panel_layout = QtWidgets.QVBoxLayout(self.decrypt_panel)
        self.decrypt_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.decrypt_panel_layout.setSpacing(0)
        self.decrypt_panel_layout.addWidget(QtWidgets.QLabel("Для расшифровки введите пароль:"))

        # User Password
        self.sd_user_password_line = QtWidgets.QLineEdit()
        self.sd_user_password_line.setMaxLength(64)
        self.sd_user_password_line.setPlaceholderText("Пользовательский пароль")
        self.sd_user_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.decrypt_panel_layout.addWidget(self.sd_user_password_line)

        # Кнопка
        self.sd_decrypt_button = QtWidgets.QPushButton("Расшифровать")
        self.sd_decrypt_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        self.decrypt_panel_layout.addWidget(self.sd_decrypt_button)
        layout.addRow(self.decrypt_panel)

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
