import hashlib

from src.api_service import APIServiceV1
from src.models.error import ErrorModel
from src.utils.encfunctions import decrypt_aes, encrypt_aes


class ProfileModel:

    def __init__(self, api: APIServiceV1, scope: dict):
        self._api_service = api
        self.scope = scope

        # список наблюдателей
        self._mObservers = []

    def logout(self):
        self.scope['main_model'].logout()

    def current_user(self) -> dict:
        response = self._api_service.current_user()
        if response.get('error'):
            self.raise_error(ErrorModel(response['error']['content'], response['error']['type']))
            return {}
        else:
            return response['message']

    def change_username(self, new_username: str, password: str):
        user = self.current_user()
        if not user:
            return

        if len(password) < 16:
            password = password + ' ' * (16 - len(password))

        old_hashed_password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), user['username'].lower().encode("utf8"), 50000, dklen=32
        ).hex()
        new_hashed_password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), new_username.lower().encode("utf8"), 50000, dklen=32
        ).hex()
        response = self._api_service.update_username(
            username=new_username,
            old_hashed_password=old_hashed_password,
            new_hashed_password=new_hashed_password
        )
        if response.get('error'):
            self.raise_error(ErrorModel(response['error']['content'], response['error']['type']))
        self.notify_observers()

    def change_password(self, new_password: str, old_password: str):
        """
            Обновление пользовательского пароля должно происходить в связке с обновлением ключей шифрования,
            так-как приватный ключ шифрования зашифрован пользовательским паролем.
        """
        user = self.current_user()
        if not user:
            return

        keys = self._api_service.get_keys()

        if len(new_password) < 16:
            new_password = new_password + ' ' * (16 - len(new_password))

        if len(old_password) < 16:
            old_password = old_password + ' ' * (16 - len(old_password))

        old_hashed_password = hashlib.pbkdf2_hmac(
            'sha256', old_password.encode('utf-8'), user['username'].lower().encode("utf8"), 50000, dklen=32
        ).hex()
        new_hashed_password = hashlib.pbkdf2_hmac(
            'sha256', new_password.encode('utf-8'), user['username'].lower().encode("utf8"), 50000, dklen=32
        ).hex()
        private_key = decrypt_aes(keys['enc_private_key'], old_password)
        new_enc_private_key = encrypt_aes(private_key, new_password)

        response = self._api_service.update_password(
            old_hashed_password=old_hashed_password,
            new_hashed_password=new_hashed_password,
            new_enc_private_key=new_enc_private_key
        )
        if response.get('error'):
            self.raise_error(ErrorModel(response['error']['content'], response['error']['type']))
        self.notify_observers()

    # def change_keys(self, new_public_key_path: str, new_private_key_path: str, password: str):
    #     user = self.current_user()
    #     if not user:
    #         return
    #
    #     if len(password) < 16:
    #         password = password + ' ' * (16 - len(password))
    #
    #
    #
    #
    #     old_hashed_password = hashlib.pbkdf2_hmac(
    #         'sha256', old_password.encode('utf-8'), user['username'].lower().encode("utf8"), 50000, dklen=32
    #     ).hex()
    #     new_hashed_password = hashlib.pbkdf2_hmac(
    #         'sha256', new_password.encode('utf-8'), user['username'].lower().encode("utf8"), 50000, dklen=32
    #     ).hex()
    #     response = self._api_service.update_password(
    #         old_hashed_password=old_hashed_password,
    #         new_hashed_password=new_hashed_password
    #     )
    #     if response.get('error'):
    #         self.raise_error(ErrorModel(response['error']['content'], response['error']['type']))
    #     self.notify_observers()

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()

    def raise_error(self, error):
        for observer in self._mObservers:
            observer.error_handler(error)
