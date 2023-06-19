from src.api_service import APIServiceV1
from src.models.error import ErrorModel
from src.utils.encfunctions import decrypt_rsa, decrypt_aes, encrypt_rsa


class DataModel:
    def __init__(self, api: APIServiceV1, scope: dict[str]):
        self._api_service = api
        self.scope = scope

        # список наблюдателей
        self._mObservers = []

        self._data = []

    @property
    def data(self) -> list[dict[str]]:
        return self._data

    @property
    def api_service(self) -> APIServiceV1:
        return self._api_service

    def load_data_list(self, page=1, per_page=100, resource_id: str = None) -> None:
        response = self._api_service.password_list(
            page=page,
            per_page=per_page,
            resource_id=resource_id if not self.scope["resource_id"] else self.scope["resource_id"]
        )
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return
        self._data = response["message"]
        self.notify_observers()

    def add_datum(self, resource_id: str, username: str, password: str):
        response = self._api_service.get_keys()
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return

        public_key = response["message"]["public_key"]
        encrypted_password = encrypt_rsa(password, public_key)

        response = self._api_service.password_new(resource_id, username, encrypted_password)
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return

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
