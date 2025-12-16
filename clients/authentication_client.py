from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class LoginRequestDict(TypedDict):
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    refreshToken: str


class AuthenticationClient(APIClient):
    def login_api(self, request: dict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)
