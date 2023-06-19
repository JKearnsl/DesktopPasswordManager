from src.api_service import APIServiceV1
from src.models.error import ErrorModel
from src.utils.encfunctions import decrypt_rsa, decrypt_aes, encrypt_rsa


class DatumModel:
    def __init__(self, api: APIServiceV1, scope: dict[str]):
        self._api_service = api
        self.scope = scope

        # список наблюдателей
        self._mObservers = []

        self._data = []

    @property
    def data(self) -> list[dict[str]]:
        return self._data

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

    def get_datum_password(self, enc_password: str, password: str = None) -> str | None:
        resource_model = self.scope["resource_model"]
        if resource_model.private_key:
            try:
                return decrypt_rsa(enc_password, resource_model.private_key)
            except ValueError:
                resource_model.private_key = None
                self.raise_error(ErrorModel("Для продолжения введите пароль", 1))
                return None

        if len(password) < 16:
            password = password + ' ' * (16 - len(password))

        response = self._api_service.get_keys()
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return None

        enc_private_key = response["message"]["enc_private_key"]
        try:
            resource_model.private_key = decrypt_aes(enc_private_key, password)
        except (UnicodeDecodeError, UnicodeEncodeError):    # todo: fix this
            self.raise_error(ErrorModel("Неверный пароль", 1))
            return None

        return decrypt_rsa(enc_password, resource_model.private_key)

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
