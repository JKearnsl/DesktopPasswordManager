import hashlib
import logging
import pickle

import httpx

from src.api_service import APIServiceV1
from src.models.enum.auth_state import AuthState
from src.models.error import ErrorModel, ErrorType
from src.utils.encfunctions import generate_keys, encrypt_aes


class LoginModel:

    def __init__(self):
        self._api_service = APIServiceV1("http://127.0.0.1:8000/api", self.get_http_session())
        self._auth_state = AuthState.SIGNIN

        # список наблюдателей
        self._mObservers = []

    @property
    def auth_state(self):
        return self._auth_state

    @property
    def api_service(self) -> APIServiceV1:
        return self._api_service

    def is_auth(self) -> bool:
        if self._api_service.current_user().get("error"):
            self._api_service.session.cookies.clear()
            return False
        return True

    def get_http_session(self) -> httpx.Client:
        session = httpx.Client()
        try:
            cookies = httpx.Cookies()
            with open("session", "rb") as file:
                jar_cookies = pickle.load(file)
            for domain, pc in jar_cookies.items():
                for path, c in pc.items():
                    for k, v in c.items():
                        cookies.set(k, v.value, domain=domain, path=path)
            session.cookies = cookies
        except (FileNotFoundError, EOFError):
            logging.info(" Файл сессии не найден")
        return session

    def switch_auth_state(self):
        if self._auth_state == AuthState.SIGNIN:
            self._auth_state = AuthState.SIGNUP
        else:
            self._auth_state = AuthState.SIGNIN
        self.notify_observers()

    def signin(self, username: str, password: str) -> bool:
        if len(password) < 16:
            password = password + ' ' * (16 - len(password))

        hashed_password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), username.lower().encode("utf8"), 50000, dklen=32
        ).hex()
        result = self._api_service.signin(username, hashed_password)
        if result.get("error"):
            self.raise_error(ErrorModel(result["error"]["content"], result["error"]["type"]))
            return False

        with open("session", "wb") as file:
            # Issues: https://github.com/encode/httpx/issues/895#issuecomment-970689380
            pickle.dump(self._api_service.session.cookies.jar.__getattribute__("_cookies"), file)
        return True

    def signup(self, username: str, password: str, repeat_password: str) -> bool:
        if password != repeat_password:
            self.raise_error(ErrorModel("Пароли не совпадают", ErrorType.MESSAGE))
            return False

        if len(password) < 8 or len(password) > 32:
            self.raise_error(ErrorModel("Пароль должен быть от 8 до 32 символов", ErrorType.MESSAGE))
            return False

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
            self.raise_error(ErrorModel(result["error"]["content"], result["error"]["type"]))
            return False

        return True

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
