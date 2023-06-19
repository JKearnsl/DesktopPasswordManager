from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class UiDatumItemModal:
    def setup_ui(self, modal: QtWidgets.QDialog):
        modal.setObjectName("UiDatumItemModal")
        modal.setModal(True)
        modal.setMinimumSize(QtCore.QSize(500, 200))
        modal.setMaximumSize(QtCore.QSize(600, 400))

        modal.setWindowTitle("Пароль")
        modal.setStyleSheet(""" 
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
        layout = QtWidgets.QVBoxLayout(modal)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setProperty("spacing", 0)
        form_layout = QtWidgets.QFormLayout()
        form_layout.setContentsMargins(20, 0, 20, 30)
        form_layout.setProperty("spacing", 0)

        # Title
        self.head_title = QtWidgets.QLabel()
        self.head_title.setStyleSheet("""
            QLabel {
                font-size: 25px;
                font-weight: bold;
                color: black;
            }
        """)
        self.head_title.setFixedHeight(50)
        self.head_title.setText("Просмотр данных")
        self.head_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.head_title)

        # Error label
        self.error_label = QtWidgets.QLabel()
        self.error_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: red;
            }
        """)
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        layout.addWidget(self.error_label)

        # Username
        self.username_line = QtWidgets.QLineEdit()
        self.username_line.setReadOnly(True)
        form_layout.addRow(QtWidgets.QLabel("Username:"), self.username_line)

        # Password
        self.password_line = QtWidgets.QLineEdit("*" * 16)
        self.password_line.setReadOnly(True)
        form_layout.addRow(QtWidgets.QLabel("Password:"), self.password_line)

        # Decrypt panel
        self.enc_password = None
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
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setProperty("spacing", 30)
        self.decrypt_panel_layout.addWidget(QtWidgets.QLabel("Для расшифровки введите пароль:"))

        # User Password
        self.user_password_line = QtWidgets.QLineEdit()
        self.user_password_line.setMaxLength(64)
        self.user_password_line.setPlaceholderText("Пользовательский пароль")
        self.user_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.decrypt_panel_layout.addWidget(self.user_password_line)

        # Кнопка
        self.decrypt_button = QtWidgets.QPushButton("Расшифровать")
        self.decrypt_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        self.decrypt_panel_layout.addWidget(self.decrypt_button)
        form_layout.addRow(self.decrypt_panel)
        layout.addLayout(form_layout)

        self.retranslateUi(modal)
        QtCore.QMetaObject.connectSlotsByName(modal)

    def retranslateUi(self, UiDatumItemModal):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))
