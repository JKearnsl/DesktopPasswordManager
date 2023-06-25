from src.api_service import APIServiceV1
from src.models.error import ErrorModel


class ResourceModel:

    def __init__(self, api: APIServiceV1, scope: dict[str]):
        self._api_service = api
        self._loaded_resources = []
        self.scope = scope

        # список наблюдателей
        self._mObservers = []

    @property
    def loaded_resources(self) -> list[dict[str]]:
        return self._loaded_resources

    @property
    def api_service(self):
        return self._api_service

    def search_resources(self, query: str = None):
        self._loaded_resources.clear()
        self.load_resources(1, per_page=100, query=query)

    def load_resources(self, page: int = 1, per_page: int = 10, query: str = None, order_by: str = "created_at"):
        response = self._api_service.resource_list(page, per_page=per_page, query=query, order_by=order_by)
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return

        for el in response["message"]:
            if el not in self._loaded_resources:
                self._loaded_resources.append(el)

        self.notify_observers()

    def add_resource(self, title: str):
        response = self._api_service.resource_new(title)
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return

    def delete_resource(self, resource_id: str):
        response = self._api_service.resource_delete(resource_id)
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return
        self._loaded_resources.clear()
        self.load_resources()
        self.notify_observers()

    def update_resource(self, resource_id: str, title: str):
        response = self._api_service.resource_update(resource_id, title)
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return
        self._loaded_resources.clear()
        self.load_resources()
        self.notify_observers()

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
