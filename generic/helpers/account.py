from __future__ import annotations

import allure

from dm_api_account.models import *
from generic.helpers.mailhog import MailhogApi
from requests import Response

try:
    from services.dm_api_account import DmApiAccount
except ImportError:
    pass


class Account:
    def __init__(self, dm_api_account: DmApiAccount):
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
    ) -> Response:
        with allure.step("Register new user"):
            response = self.dm_api_account.account_api.register(
                registration=Registration(
                    login=login,
                    email=email,
                    password=password
                )
            )

        return response

    def activate_registered_user(self, login: str):
        token = self.dm_api_account.mailhog.get_token_by_login(login=login)
        response = self.dm_api_account.account_api.activate(token=token)

        return response

    def get_current_user_info(self, **kwargs) -> UserDetailsEnvelope | Response:
        response = self.dm_api_account.account_api.get_currentt(**kwargs)

        return response

    def reset_user_password(
            self,
            login: str,
            email: str
    ) -> Response:
        with allure.step("Reset user password"):
            response = self.dm_api_account.account_api.reset_password(
                reset_password=ResetPassword(
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
    ) -> Response:
        mailhog = MailhogApi()
        token = mailhog.get_reset_token(login=login)

        with allure.step("Change user password"):
            response = self.dm_api_account.account_api.change_password(
                change_password=ChangePassword(
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
    ) -> Response:
        with allure.step("Change user email"):
            response = self.dm_api_account.account_api.change_email(
                change_email=ChangeEmail(
                    login=login,
                    password=password,
                    email=email
                )
            )

        return response
