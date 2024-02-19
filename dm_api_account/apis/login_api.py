from requests import Response
from dm_api_account.models.login_credentials_model import login_credentials_model
from rest_client.rest_client import RestClient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)

        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: login_credentials_model, **kwargs) -> Response:
        """
        Authenticate via credentials
        :param json: change_credentials_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account/login",
            json=json,
            **kwargs
        )

        return response

    def delete_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            url=f"/v1/account/login",
            **kwargs
        )

        return response

    def delete_v1_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            url=f"/v1/account/login/all",
            **kwargs
        )

        return response
