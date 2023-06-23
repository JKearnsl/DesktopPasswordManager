from src.api_service import APIServiceV1
from src.models.error import ErrorModel


class ProfileModel:

    def __init__(self, api: APIServiceV1, scope: dict):
        self._api_service = api
        self.scope = scope

        # список наблюдателей
        self._mObservers = []

    def logout(self):
        self.scope['main_model'].logout()

    def current_user(self) -> dict:
        response = self._api_service.current_user()
        if response.get('error'):
            self.raise_error(ErrorModel(response['error']['content'], response['error']['type']))
            return {}
        else:
            return response['message']

    def change_username(self, new_username: str):
        response = self._api_service.update_user(username=new_username)
        if response.get('error'):
            self.raise_error(ErrorModel(response['error']['content'], response['error']['type']))
        self.notify_observers()

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
