from __future__ import annotations

from dm_api_account.models import Registration, ChangeEmail, ChangePassword, ResetPassword, UserDetailsEnvelope
from generic.helpers.mailhog import MailhogApi
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
            password: str,
            status_code: int
    ):
        response = self.dm_api_account.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            ), status_code=status_code
        )

        return response

    def activate_registered_user(self, login: str):
        token = self.dm_api_account.mailhog.get_token_by_login(login=login)
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
            old_password: str,
            new_password: str,
            **kwargs
    ):
        mailhog = MailhogApi()
        token = mailhog.get_reset_token(login=login)

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
