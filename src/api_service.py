from json import JSONDecodeError

import httpx


class APIServiceV1:
    def __init__(self, base_url: str, session: httpx.Client):
        self._session = session
        self._base_url = base_url + "/v1/"

    @property
    def session(self):
        return self._session

    def signup(self, username: str, hashed_password: str, public_key: str, enc_private_key: str):
        try:
            result = self._session.post(
                self._base_url + "auth/signUp",
                json=dict(
                    username=username,
                    hashed_password=hashed_password,
                    public_key=public_key,
                    enc_private_key=enc_private_key
                )
            )
            if result.status_code == 201:
                return dict(message="ok")
            else:
                return result.json()

        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def signin(self, username: str, hashed_password: str):
        try:
            return self._session.post(
                self._base_url + "auth/signIn",
                json=dict(
                    username=username,
                    hashed_password=hashed_password,
                ),
            ).json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def logout(self):
        try:
            result = self._session.post(self._base_url + "auth/logout")
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def refresh_tokens(self):
        try:
            result = self._session.post(self._base_url + "auth/refresh_tokens")
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def current_user(self):
        try:
            return self._session.get(self._base_url + "user/current").json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def update_username(self, username: str, new_hashed_password: str, old_hashed_password: str):
        """
        Обновление пользовательского имени происходит с требованием передачи
        - Старого хеша - хеша, на основе пароля + соли основанной на старом имени пользователя.
        - Нового хеша - хеша, на основе пароля + соли основанной на новом имени пользователя.

        Причем сертификаты меня не требуется, так как шифруются с помощью пароля по AES
        """

        try:
            result = self._session.put(
                self._base_url + "user/update/username",
                json=dict(
                    username=username,
                    new_hashed_password=new_hashed_password,
                    old_hashed_password=old_hashed_password,
                )
            ).json()
            return result
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def update_password(self, new_hashed_password: str, old_hashed_password: str, new_enc_private_key: str):
        try:
            result = self._session.put(
                self._base_url + "user/update/password",
                params=dict(
                    new_hashed_password=new_hashed_password,
                    old_hashed_password=old_hashed_password,
                    new_enc_private_key=new_enc_private_key,
                )
            ).json()
            return result
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def update_keys(self, public_key: str, enc_private_key: str, hashed_password: str):
        """
        Обновление пользовательских ключей шифрования должно происходить в связке с перешифровкой всех данных
        """

        try:
            result = self._session.put(
                self._base_url + "user/update/keys",
                json=dict(
                    public_key=public_key,
                    enc_private_key=enc_private_key,
                    hashed_password=hashed_password,
                )
            ).json()
            return result
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def get_keys(self):
        try:
            return self._session.get(self._base_url + "user/keys").json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def delete_user(self):
        try:
            result = self._session.delete(self._base_url + "user/delete")
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def resource_list(self, page: int = 1, per_page: int = 10, query: str = None, order_by: str = "created_at"):
        try:
            return self._session.get(
                self._base_url + "resource/list",
                params=dict(
                    page=page,
                    per_page=per_page,
                    query=query,
                    order_by=order_by
                )
            ).json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def resource_new(self, title: str):
        try:
            return self._session.post(self._base_url + "resource/new", json=dict(title=title)).json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def password_list(self, resource_id: str, page: int = 1, per_page: int = 10):
        try:
            return self._session.get(
                self._base_url + "password/list",
                params=dict(
                    resource_id=resource_id,
                    page=page,
                    per_page=per_page
                )
            ).json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def password_new(self, resource_id: str, username: str, enc_password: str):
        try:
            result = self._session.post(
                self._base_url + "password/new",
                params=dict(
                    resource_id=resource_id,
                ),
                json=dict(
                    username=username,
                    enc_password=enc_password
                )
            )
            if result.status_code == 201:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def resource_delete(self, resource_id: str):
        try:
            result = self._session.delete(self._base_url + "resource/delete", params=dict(resource_id=resource_id))
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def resource_update(self, resource_id: str, title: str):
        try:
            result = self._session.put(
                self._base_url + "resource/update",
                params=dict(resource_id=resource_id),
                json=dict(title=title)
            )
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def delete_datum(self, datum_id: str):
        try:
            result = self._session.delete(self._base_url + "password/delete", params=dict(datum_id=datum_id))
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))

    def update_datum(self, datum_id: str, username: str, enc_password: str):
        try:
            result = self._session.put(
                self._base_url + "password/update",
                params=dict(datum_id=datum_id),
                json=dict(
                    username=username,
                    enc_password=enc_password
                )
            )
            if result.status_code == 204:
                return dict(message="ok")
            else:
                return result.json()
        except (httpx.ConnectError, httpx.TimeoutException):
            return dict(error=dict(content="Ошибка соединения", type=1))
        except JSONDecodeError:
            return dict(error=dict(content="Неизвестная ошибка", type=1))
