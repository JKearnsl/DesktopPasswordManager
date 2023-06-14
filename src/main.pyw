import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QStyleFactory

from src.models.login import LoginModel
from src.models.main import MainModel
from src.controllers.login import LoginController
from src.controllers.main import MainController


def main():
    QApplication.setDesktopSettingsAware(False)
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    QtCore.QDir.addSearchPath('icons', 'assets/window/icons')

    login_model = LoginModel()
    if not login_model.is_auth():
        controller = LoginController(login_model)
    else:
        main_model = MainModel()
        controller = MainController(main_model)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
