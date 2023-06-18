from src.api_service import APIServiceV1


class ProfileModel:

    def __init__(self, api: APIServiceV1):
        self._api_service = api
        self._errors = []

        # список наблюдателей
        self._mObservers = []

    @property
    def errors(self):
        return self._errors


    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
