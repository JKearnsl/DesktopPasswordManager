from src.api_service import APIServiceV1
from src.models.error import ErrorModel
from src.utils.encfunctions import decrypt_rsa, decrypt_aes


class CPModel:
    def __init__(self, api: APIServiceV1):
        self._api_service = api

        # список наблюдателей
        self._mObservers = []

    def change_password(self, old_password: str, new_password: str) -> None:
        pass

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()

    def raise_error(self, error: ErrorModel):
        for observer in self._mObservers:
            observer.error_handler(error)
