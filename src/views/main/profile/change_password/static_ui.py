from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class UiCPModal:
    def setup_ui(self, modal: QtWidgets.QDialog):
        modal.setObjectName("UiCPModal")
        modal.setModal(True)
        modal.setMinimumSize(QtCore.QSize(500, 200))
        modal.setMaximumSize(QtCore.QSize(600, 400))

        modal.setWindowTitle("Смена пароля")
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

        # Password
        self.password_line = QtWidgets.QLineEdit()
        self.password_line.setReadOnly(True)
        form_layout.addRow(QtWidgets.QLabel("Password:"), self.password_line)

        # New password
        self.new_password_line = QtWidgets.QLineEdit()
        self.new_password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.new_password_line.setPlaceholderText("Новый пароль")
        form_layout.addRow(QtWidgets.QLabel("New password:"), self.new_password_line)

        # Кнопка
        self.cp_button = QtWidgets.QPushButton("Сменить пароль")
        self.cp_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor("#d1d1d1"),
            offset=QtCore.QPointF(0, 0)
        ))
        form_layout.addRow(self.cp_button)
        layout.addLayout(form_layout)

        self.retranslateUi(modal)
        QtCore.QMetaObject.connectSlotsByName(modal)

    def retranslateUi(self, UiDatumItemModal):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))
