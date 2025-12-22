from typing import TypedDict

from httpx import Response

from api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
           Клиент для работы с /api/v1/users
           """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
                       Метод позволяет создать пользователя.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.client.post('/api/v1/users', json=request)
