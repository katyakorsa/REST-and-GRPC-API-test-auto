from __future__ import annotations

from dm_api_account.models import Registration, ChangeEmail, ChangePassword, ResetPassword, UserDetailsEnvelope
from requests import Response


class Account:
    def __init__(self, dm_api_account):
        from services.dm_api_account import DmApiAccount
        self.dm_api_account: DmApiAccount = dm_api_account
        # self.dm_api_account = dm_api_account

    def set_headers(self, headers):
        self.dm_api_account.account_api.client.session.headers.update(headers)

    def register_new_user(
            self,
            login: str,
            email: str,
            password: str
    ):
        response = self.dm_api_account.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )

        return response

    def activate_registered_user(self, ):
        token = self.dm_api_account.mailhog.get_token_from_last_email()
        response = self.dm_api_account.account_api.put_v1_account_token(token=token)

        return response

    def get_current_user_info(self, **kwargs) -> UserDetailsEnvelope | Response:
        response = self.dm_api_account.account_api.get_v1_account(**kwargs)

        return response

    def reset_user_password(
            self,
            login: str,
            email: str
    ):
        response = self.dm_api_account.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            )
        )

        return response

    def change_user_password(
            self,
            login: str,
            token: str,
            old_password: str,
            new_password: str,
            **kwargs
    ):
        response = self.dm_api_account.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                oldPassword=old_password,
                newPassword=new_password
            ), **kwargs
        )

        return response

    def change_user_email(
            self,
            login: str,
            password: str,
            email: str
    ):
        response = self.dm_api_account.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                password=password,
                email=email
            )
        )

        return response
