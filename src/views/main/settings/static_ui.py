from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_settingsMenu(object):
    def setupUi(self, settingsMenu):
        settingsMenu.setObjectName("settingsMenu")
        self.central_layout = QtWidgets.QHBoxLayout(settingsMenu)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setObjectName("central_layout")

        self.content_widget = QtWidgets.QWidget(settingsMenu)
        self.content_widget.setObjectName("content_widget")
        self.content_widget.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                border: none;
            }
        """)
        self.content_widget.setMaximumWidth(300)
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")

        self.central_layout.addWidget(self.content_widget)

        self.retranslateUi(settingsMenu)
        QtCore.QMetaObject.connectSlotsByName(settingsMenu)

    def retranslateUi(self, settingsMenu):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "CompMath"))
