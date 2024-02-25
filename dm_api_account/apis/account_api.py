from requests import Response
from dm_api_account.models.registration_model import RegistrationModel
from dm_api_account.models.reset_password_model import ResetPasswordModel
from dm_api_account.models.change_password_model import ChangePasswordModel
from dm_api_account.models.change_email_model import ChangeEmailModel
from dm_api_account.models.user_details_envelope_model import UserDetailsEnvelopeModel
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
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
        UserDetailsEnvelopeModel(**response.json())

        return response

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        Register new user
        :param json: registration_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )

        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """

        response = self.client.post(
            url=f"/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())

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
        UserEnvelopeModel(**response.json())

        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """

        response = self.client.put(
            url=f"/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())

        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """

        response = self.client.put(
            url=f"/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())

        return response
