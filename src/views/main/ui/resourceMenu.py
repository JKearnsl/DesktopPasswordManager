from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_resourcesMenu(object):
    def setupUi(self, settingsMenu):
        settingsMenu.setObjectName("settingsMenu")
        self.central_layout = QtWidgets.QHBoxLayout(settingsMenu)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setObjectName("central_layout")

        # Разделитель
        self.separator = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.separator.setObjectName("separator")
        self.separator.setContentsMargins(0, 0, 0, 0)

        # Панель ресурсов
        self.resource_panel = QtWidgets.QListWidget()
        self.resource_panel.setObjectName("resource_panel")
        self.resource_panel.setContentsMargins(0, 0, 0, 0)
        self.resource_panel.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 1px solid black;
            }
        """)
        self.resource_panel.setMinimumWidth(100)
        self.rp_layout = QtWidgets.QVBoxLayout(self.resource_panel)
        self.rp_layout.setObjectName("rp_layout")
        self.rp_layout.setContentsMargins(0, 0, 0, 0)
        self.resource_panel.setLayout(self.rp_layout)
        self.separator.addWidget(self.resource_panel)

        # Панель данных
        self.datum_panel = QtWidgets.QWidget()
        self.datum_panel.setObjectName("datum_panel")
        self.datum_panel.setContentsMargins(0, 0, 0, 0)
        self.datum_panel.setStyleSheet("""
            QWidget {
                border: 1px solid black;
            }
        """)
        self.datum_panel.setMinimumWidth(100)
        self.dp_layout = QtWidgets.QVBoxLayout(self.datum_panel)
        self.dp_layout.setObjectName("dp_layout")
        self.dp_layout.setContentsMargins(0, 0, 0, 0)
        self.datum_panel.setLayout(self.dp_layout)
        self.separator.addWidget(self.datum_panel)

        self.central_layout.addWidget(self.separator)

        self.retranslateUi(settingsMenu)
        QtCore.QMetaObject.connectSlotsByName(settingsMenu)

    def retranslateUi(self, settingsMenu):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))

