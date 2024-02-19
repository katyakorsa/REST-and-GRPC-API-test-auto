from requests import Response
from dm_api_account.models.registration_model import registration_model
from dm_api_account.models import reset_password_model
from dm_api_account.models.change_password_model import change_password_model
from dm_api_account.models.change_email_model import change_email_model
from rest_client.rest_client import RestClient


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)

        if headers:
            self.client.session.headers.update(headers)

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            url=f"/v1/account",

            **kwargs
        )

        return response

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        Register new user
        :param json: registration_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account",
            json=json,
            **kwargs
        )

        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_token(self, token, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """

        response = self.client.put(
            url=f"/v1/account/{token}",
            **kwargs
        )

        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """

        response = self.client.put(
            url=f"/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_email(self, json: change_email_model, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """

        response = self.client.put(
            url=f"/v1/account/email",
            json=json,
            **kwargs
        )

        return response
