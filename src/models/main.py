import pickle

from src.api_service import APIServiceV1


class MainModel:

    def __init__(self, api: APIServiceV1):
        self._api_service = api
        self._loaded_resources = []
        self._errors = []

        # список наблюдателей
        self._mObservers = []

    @property
    def loaded_resources(self) -> list[dict[str]]:
        return self._loaded_resources

    @property
    def errors(self):
        return self._errors

    def load_resources(self, page: int, query: str = None, order_by: str = "created_at"):
        response = self._api_service.resource_list(page, query=query, order_by=order_by)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])

        self._loaded_resources = response["message"]["content"]

    def add_resource(self, title: str):
        response = self._api_service.resource_new(title)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])

    def save_session(self):
        with open("session", "wb") as file:
            # Issues: https://github.com/encode/httpx/issues/895#issuecomment-970689380
            pickle.dump(self._api_service.session.cookies.jar.__getattribute__("_cookies"), file)

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
