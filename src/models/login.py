import hashlib
import logging
import pickle

import httpx

from src.api_service import APIServiceV1
from src.models.enum.auth_state import AuthState
from src.utils.encfunctions import generate_keys, encrypt_aes


class LoginModel:

    def __init__(self):
        self._api_service = APIServiceV1("http://127.0.0.1:8000/api", self.get_http_session())
        self._auth_state = AuthState.SIGNIN
        self._errors = []

        # список наблюдателей
        self._mObservers = []

    @property
    def auth_state(self):
        return self._auth_state

    @property
    def errors(self):
        return self._errors

    def is_auth(self) -> bool:
        if self._api_service.current_user().get("error"):
            self._api_service.session.cookies.clear()
            return False
        return True

    def get_http_session(self) -> httpx.Client:
        session = httpx.Client()
        try:
            with open("session", "rb") as file:
                session.cookies.update(pickle.load(file))
        except (FileNotFoundError, EOFError):
            logging.info(" Файл сессии не найден")
        return session

    def switch_auth_state(self):
        if self._auth_state == AuthState.SIGNIN:
            self._auth_state = AuthState.SIGNUP
        else:
            self._auth_state = AuthState.SIGNIN
        self.notify_observers()

    def signin(self, username: str, password: str):
        if len(password) < 16:
            password = password + ' ' * (16 - len(password))

        hashed_password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), username.lower().encode("utf8"), 50000, dklen=32
        ).hex()
        result = self._api_service.signin(username, hashed_password)
        if result.get("error"):
            if result["error"]["type"] == 1:
                self._errors.append(result["error"]["content"])
            else:
                self._errors.append("тип 2")
            self.notify_observers()
            return False

        # todo: в main приложении
        with open("session", "wb") as file:
            pickle.dump({key: value for key, value in self._api_service.session.cookies.items()}, file)

        return True

    def signup(self, username: str, password: str, repeat_password: str):
        if password != repeat_password:
            self._errors.append("Пароли не совпадают")
            self.notify_observers()
            return

        if len(password) < 8 or len(password) > 32:
            self._errors.append("Длина пароля должна быть от 8 до 32 символов")
            self.notify_observers()
            return

        if len(password) < 16:
            """
            Для того чтобы зашифровать приватный ключ при помощи AES алгоритма,
            нужен ключ > 128 бит или 16 байт
    
            """
            password = password + ' ' * (16 - len(password))

        hashed_password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), username.lower().encode("utf8"), 50000, dklen=32
        ).hex()

        private_key, public_key = generate_keys(2136)
        enc_private_key = encrypt_aes(private_key, password)

        result = self._api_service.signup(username, hashed_password, public_key, enc_private_key)
        if result.get("error"):
            if result["error"]["type"] == 1:
                self._errors.append(result["error"]["content"])
            else:
                self._errors.append("Тип 2")
            self.notify_observers()
            return

        self.switch_auth_state()

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
