from src.api_service import APIServiceV1
from src.utils.encfunctions import encrypt_rsa, decrypt_aes, decrypt_rsa


class ResourceModel:

    def __init__(self, api: APIServiceV1):
        self._api_service = api
        self._loaded_resources = []
        self._data = []
        self._private_key = None
        self._errors = []

        # список наблюдателей
        self._mObservers = []

    @property
    def loaded_resources(self) -> list[dict[str]]:
        return self._loaded_resources

    @property
    def data(self) -> list[dict[str]]:
        return self._data

    @property
    def errors(self):
        return self._errors

    def search_resources(self, query: str = None):
        self._loaded_resources.clear()
        self.load_resources(1, per_page=100, query=query)

    def load_resources(self, page: int = 1, per_page: int = 10, query: str = None, order_by: str = "created_at"):
        response = self._api_service.resource_list(page, per_page=per_page, query=query, order_by=order_by)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])
            return

        if not response["message"]:
            return

        for el in response["message"]:
            if el not in self._loaded_resources:
                self._loaded_resources.append(el)

        self.notify_observers()

    def add_resource(self, title: str):
        response = self._api_service.resource_new(title)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])

    def add_datum(self, resource_id: str, username: str, password: str):
        response = self._api_service.get_keys()
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])
            return

        public_key = response["message"]["public_key"]
        encrypted_password = encrypt_rsa(password, public_key)

        response = self._api_service.password_new(resource_id, username, encrypted_password)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])
            return
        self.notify_observers()

    def get_datum_password(self, enc_password: str, password: str = None) -> str | None:
        if self._private_key:
            try:
                return decrypt_rsa(enc_password, self._private_key)
            except ValueError:
                pass

        if len(password) < 16:
            password = password + ' ' * (16 - len(password))

        response = self._api_service.get_keys()
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])
            return

        enc_private_key = response["message"]["enc_private_key"]
        self._private_key = decrypt_aes(enc_private_key, password)

        return decrypt_rsa(enc_password, self._private_key)

    def load_resource(self, resource_id: str):
        response = self._api_service.password_list(page=1, per_page=100, resource_id=resource_id)
        if response.get("error"):
            if response["error"]["type"] == 1:
                self._errors.append(response["error"]["content"])
            else:
                print("error2", response["error"]["content"])
            return

        self._data = response["message"]
        self.notify_observers()

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
