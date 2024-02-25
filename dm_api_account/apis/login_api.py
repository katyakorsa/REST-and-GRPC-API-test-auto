from requests import Response
from dm_api_account.models.login_credentials_model import LoginCredentialsModel
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from rest_client.rest_client import RestClient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)

        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentialsModel, **kwargs) -> Response:
        """
        Authenticate via credentials
        :param json: change_credentials_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account/login",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())

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
