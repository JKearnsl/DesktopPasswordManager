from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class UiSettingsMenu(object):
    def setup_ui(self, settings_menu):
        settings_menu.setObjectName("settings_menu")
        self.central_layout = QtWidgets.QHBoxLayout(settings_menu)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addItem(
            QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.content_widget = QtWidgets.QWidget(settings_menu)
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
        """)
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

        # Settings form
        self.settings_form = QtWidgets.QFormLayout()
        self.settings_form.setContentsMargins(20, 0, 20, 0)
        self.settings_form.setVerticalSpacing(20)
        self.settings_form.setHorizontalSpacing(10)
        self.content_layout.addLayout(self.settings_form)

        # Scale factor
        self.scaling_label = QtWidgets.QLabel(self.content_widget)
        self.scaling_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: black;
            }
        """)

        self.scaling_slider = QtWidgets.QComboBox(self.content_widget)
        self.scaling_slider.setStyleSheet("""
            QComboBox {
                font-size: 18px;
                font-weight: bold;
                color: black;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                padding: 5px;
            }
            
            QComboBox::drop-down {
                border: 1px solid #e0e0e0;
            }
            
            QComboBox:disabled {
                background-color: #d1d1d1;
                color: #a1a1a1;
            }    
        """)
        self.scaling_slider.addItems(['Auto', '100%', '125%', '150%', '175%', '200%'])
        self.scaling_slider.setCurrentIndex(0)
        self.scaling_slider.setDisabled(True)
        self.scaling_slider.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            color=QtGui.QColor(0, 0, 0, 25),
            offset=QtCore.QPointF(0, 0)
        ))

        self.settings_form.addRow(self.scaling_label, self.scaling_slider)

        self.content_layout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        )

        self.central_layout.addWidget(self.content_widget)

        self.central_layout.addItem(
            QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        )
        self.translate_ui(settings_menu)
        QtCore.QMetaObject.connectSlotsByName(settings_menu)

    def translate_ui(self, settings_menu):
        _translate = QtCore.QCoreApplication.translate
        self.title_label.setText(_translate("SettingsTitle", "Настройки"))
        self.scaling_label.setText(_translate("SettingsScalingLabel", "Масштабирование интерфейса:"))
