from __future__ import annotations

from requests import Response

from utils.utils import validate_request_json, validate_status_code
from ..models import *
from rest_client.rest_client import RestClient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)

        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(
            self,
            json: LoginCredentials,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Authenticate via credentials
        :param status_code:
        :param json: change_credentials_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account/login",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)

        # if response.status_code == 200:
        #     return UserEnvelope(**response.json())

        return response

    def delete_v1_account_login(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            url=f"/v1/account/login",
            **kwargs
        )
        validate_status_code(response, status_code)

        return response

    def delete_v1_account_login_all(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            url=f"/v1/account/login/all",
            **kwargs
        )
        validate_status_code(response, status_code)

        return response
