from src.views.main import MainView


class MainController:

    def __init__(self, model: 'MainModel'):
        self.model = model
        self.view = MainView(self, self.model)

        self.view.show()

