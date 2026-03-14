from dataclasses import dataclass

import pytest
import requests

from constants import create_user_endpoint, delete_user_endpoint
from helpers.build_user import BuildUser

@dataclass
class UserResponse:
    user_data: dict
    token: str

def create_user():
    endpoint = create_user_endpoint()
    user_data = BuildUser.build_user()

    response = requests.post(endpoint, data=user_data)

    if response.status_code != 200:
        pytest.fail(
            f"Регистрация не прошла. Статус: {response.status_code}, тело: {response.body}")

    return UserResponse(user_data=user_data, token=response.json()["accessToken"])


def delete_user(token: str = None):
    endpoint = delete_user_endpoint()
    requests.session().headers.update({"Content-Type": "application/json"})
    merged_headers = dict(requests.session().headers) | ({"Authorization": f"{token}"} if token else {})

    response = requests.delete(endpoint, headers=merged_headers)
    if response.status_code != 202:
        pytest.fail(f"Удаление пользователя не прошло. Статус: {response.status_code}, тело: {response.json()}")

