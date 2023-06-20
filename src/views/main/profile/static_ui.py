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
                        background-color: #f5f5f5;
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
                """)
        self.title_label.setText("Профиль")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_layout.addWidget(self.title_label)

        # Settings form
        self.settings_form = QtWidgets.QFormLayout()
        self.settings_form.setContentsMargins(20, 0, 20, 0)
        self.settings_form.setVerticalSpacing(20)
        self.settings_form.setHorizontalSpacing(10)
        self.content_layout.addLayout(self.settings_form)

        # ...

        self.content_layout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        # logout button
        self.logout_button = QtWidgets.QPushButton(self.content_widget)
        self.logout_button.setStyleSheet("""
                    QPushButton {
                        background-color: #f5f5f5;
                        border: none;
                        font-size: 18px;
                        font-weight: bold;
                        color: #ff0000;
                        padding: 10px;
                    }

                    QPushButton:hover {
                        background-color: #ff0000;
                        color: #f5f5f5;
                    }
                """)
        self.logout_button.setText("Выйти")
        self.logout_button.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))
        self.content_layout.addWidget(self.logout_button)

        self.central_layout.addWidget(self.content_widget)

        self.central_layout.addItem(
            QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.retranslateUi(profile_menu)
        QtCore.QMetaObject.connectSlotsByName(profile_menu)

    def retranslateUi(self, profile_menu):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))

