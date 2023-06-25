from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class UiProfileMenu:
    def setup_ui(self, profile_menu):
        profile_menu.setObjectName("profile_menu")
        self.central_layout = QtWidgets.QHBoxLayout(profile_menu)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addItem(
            QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.content_widget = QtWidgets.QWidget(profile_menu)
        self.content_widget.setObjectName("content_widget")
        self.content_widget.setStyleSheet("""
            QWidget {
                background-color: white;
                border: none;
            }
        """)
        self.content_widget.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_widget.setMinimumWidth(500)
        self.content_widget.setMaximumWidth(1000)
        self.content_widget.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        # Content

        # Title
        self.title_label = QtWidgets.QLabel(self.content_widget)
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: black;
                padding: 20px;
                border-bottom: 1px solid #e0e0e0;
            }
        """)  # "border: none; border-bottom: 1px solid #e0e0e0;" - bug
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_layout.addWidget(self.title_label)
        self.content_layout.addItem(
            QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        # Error label
        self.error_label = QtWidgets.QLabel(self.content_widget)
        self.error_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: red;
            }
        """)
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setText('')
        self.error_label.setHidden(True)
        self.content_layout.addWidget(self.error_label)
        self.content_layout.addItem(
            QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        # Settings form
        self.settings_form = QtWidgets.QFormLayout()
        self.settings_form.setContentsMargins(20, 0, 20, 0)
        self.settings_form.setVerticalSpacing(20)
        self.settings_form.setHorizontalSpacing(10)
        self.settings_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.settings_form.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.content_layout.addLayout(self.settings_form)

        # Username
        self.username_label = QtWidgets.QLabel(self.content_widget)
        self.username_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: black;
                padding: 10px;
            }
        """)
        self.settings_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.username_label)
        self.username_input = QtWidgets.QLineEdit(self.content_widget)
        self.username_input.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                font-weight: bold;
                background-color: white;
                color: black;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        self.settings_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.username_input)

        self.settings_form.addItem(
            QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        # save button
        self.save_button = QtWidgets.QPushButton(self.content_widget)
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                color: #1ca21e;
                border-radius: 7px;
                border: 1px solid #d1d1d1;
                padding: 5px;
                margin-bottom: 2px;
                margin-top: 2px;
            }
            
            QPushButton:hover {
                background-color: #71ab72;
                color: white;
            }
            
            QPushButton:pressed {
                background-color: white;
                color: green;
            }
        """)
        self.save_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.settings_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.save_button)



        self.content_layout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        )

        # change password button
        self.change_password_button = QtWidgets.QPushButton(self.content_widget)
        self.change_password_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                color: #ff0000;
                border-radius: 7px;
                border: 1px solid #d1d1d1;
                padding: 5px;
                margin-left: 25px;
                margin-right: 25px;
                margin-bottom: 2px;
                margin-top: 2px;
            }

            QPushButton:hover {
                background-color: #ff0000;
                color: white;
            }

            QPushButton:pressed {
                background-color: white;
                color: #ff0000;
            }
            
            QPushButton:disabled {
                background-color: white;
                color: #d1d1d1;
            }
        """)
        self.change_password_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_layout.addWidget(self.change_password_button)

        # change Cert button
        self.change_keys_button = QtWidgets.QPushButton(self.content_widget)
        self.change_keys_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                color: #ff0000;
                border-radius: 7px;
                border: 1px solid #d1d1d1;
                padding: 5px;
                margin-left: 25px;
                margin-right: 25px;
                margin-bottom: 2px;
                margin-top: 2px;
            }
            
            QPushButton:hover {
                background-color: #ff0000;
                color: white;
            }
            
            QPushButton:pressed {
                background-color: white;
                color: #ff0000;
            }
            
            QPushButton:disabled {
                background-color: white;
                color: #d1d1d1;
            }
        """)
        self.change_keys_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_layout.addWidget(self.change_keys_button)

        # logout button
        self.logout_button = QtWidgets.QPushButton(self.content_widget)
        self.logout_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                font-size: 16px;
                font-weight: bold;
                color: #ff0000;
                border-radius: 7px;
                border: 1px solid #d1d1d1;
                padding: 5px;
                margin-left: 25px;
                margin-right: 25px;
                margin-bottom: 2px;
                margin-top: 2px;
            }

            QPushButton:hover {
                background-color: #ff0000;
                color: white;
            }

            QPushButton:pressed {
                background-color: white;
                color: #ff0000;
            }
        """)
        self.logout_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_layout.addWidget(self.logout_button)
        self.content_layout.addItem(
            QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        )

        self.central_layout.addWidget(self.content_widget)

        self.central_layout.addItem(
            QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.translate_ui(profile_menu)
        QtCore.QMetaObject.connectSlotsByName(profile_menu)

    def translate_ui(self, profile_menu):
        _translate = QtCore.QCoreApplication.translate
        self.change_keys_button.setText(_translate("profile_menu", "Изменить RSA ключи"))
        self.change_password_button.setText(_translate("profile_menu", "Изменить пароль"))
        self.logout_button.setText(_translate("profile_menu", "Выйти"))
        self.save_button.setText(_translate("profile_menu", "Сохранить"))
        self.title_label.setText(_translate("profile_menu", "Профиль"))
        self.username_input.setPlaceholderText(_translate("profile_menu", "Введите имя пользователя"))
        self.username_label.setText(_translate("profile_menu", "Имя пользователя"))


