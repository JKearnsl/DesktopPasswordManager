import os
import pickle

from src.api_service import APIServiceV1
from src.models.error import ErrorModel


class MainModel:

    def __init__(self, api: APIServiceV1):
        self._api_service = api
        self._private_key = None

        # список наблюдателей
        self._mObservers = []

    @property
    def api_service(self) -> APIServiceV1:
        return self._api_service

    @property
    def private_key(self) -> str | None:
        return self._private_key

    @private_key.setter
    def private_key(self, value):
        self._private_key = value

    def save_session(self):
        with open("session", "wb") as file:
            # Issues: https://github.com/encode/httpx/issues/895#issuecomment-970689380
            pickle.dump(self._api_service.session.cookies.jar.__getattribute__("_cookies"), file)

    def logout(self):
        with open("session", "wb") as file:
            file.truncate(0)
        self._api_service.session.cookies.clear()
        del self

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
