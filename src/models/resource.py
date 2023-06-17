from src.api_service import APIServiceV1


class ResourceModel:

    def __init__(self, api: APIServiceV1):
        self._api_service = api
        self._loaded_resources = []
        self._errors = []

        self.load_resources()

        # список наблюдателей
        self._mObservers = []

    @property
    def loaded_resources(self) -> list[dict[str]]:
        return self._loaded_resources

    @property
    def errors(self):
        return self._errors

    def load_resources(self, page: int = 1, query: str = None, order_by: str = "created_at"):
        response = self._api_service.resource_list(page, query=query, order_by=order_by)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])

        self._loaded_resources = response["message"]

    def add_resource(self, title: str):
        response = self._api_service.resource_new(title)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])
        self.notify_observers()

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
