from src.api_service import APIServiceV1
from src.models.error import ErrorModel
from src.utils.encfunctions import decrypt_rsa, decrypt_aes


class DatumModel:
    def __init__(self, api: APIServiceV1, scope: dict[str]):
        self._api_service = api
        self.scope = scope

        self.id = scope["datum_id"]
        self.username = scope["datum_username"]
        self.enc_password = scope["datum_enc_password"]
        self.dec_password = None

        # список наблюдателей
        self._mObservers = []

    def decrypt_datum_password(self, user_password: str = None) -> None:
        resource_model = self.scope["resource_model"]
        if resource_model.private_key:
            try:
                self.dec_password = decrypt_rsa(self.enc_password, resource_model.private_key)
                self.notify_observers()
                return
            except ValueError:
                resource_model.private_key = None
                self.raise_error(ErrorModel("Для продолжения введите пароль", 1))
                return

        if len(user_password) < 16:
            user_password = user_password + ' ' * (16 - len(user_password))

        response = self._api_service.get_keys()
        if response.get("error"):
            self.raise_error(ErrorModel(response["error"]["content"], response["error"]["type"]))
            return

        enc_private_key = response["message"]["enc_private_key"]
        try:
            resource_model.private_key = decrypt_aes(enc_private_key, user_password)
        except (UnicodeDecodeError, UnicodeEncodeError):    # todo: fix this
            self.raise_error(ErrorModel("Неверный пароль", 1))
            return

        self.dec_password = decrypt_rsa(self.enc_password, resource_model.private_key)
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
