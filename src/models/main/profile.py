from src.api_service import APIServiceV1


class ProfileModel:

    def __init__(self, api: APIServiceV1, scope: dict):
        self._api_service = api
        self.scope = scope

        # список наблюдателей
        self._mObservers = []

    def logout(self):
        self.scope['main_model'].logout()

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()

    def raise_error(self, error):
        for observer in self._mObservers:
            observer.error_handler(error)