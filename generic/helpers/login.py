import allure
from requests import Response

from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, dm_api_account):
        from services.dm_api_account import DmApiAccount
        self.dm_api_account: DmApiAccount = dm_api_account

    def set_headers(self, headers) -> None:
        self.dm_api_account.login_api.client.session.headers.update(headers)

    def login_user(
            self,
            login: str,
            password: str,
            remember_me: bool
    ) -> Response:
        with allure.step("User login"):
            response = self.dm_api_account.login_api.v1_account_login_post(
                login_credentials=LoginCredentials(
                    login=login,
                    password=password,
                    remember_me=remember_me
                )
            )

        return response

    def get_auth_token(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        with allure.step("Get auth token"):
            response = self.login_user(login=login, password=password, remember_me=remember_me)

        return {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}

    def logout_user(self, **kwargs):
        with allure.step("User logout"):
            return self.dm_api_account.login_api.v1_account_login_delete(**kwargs)

    def logout_from_every_device(self, **kwargs):
        with allure.step("Logout from every device"):
            return self.dm_api_account.login_api.v1_account_login_all_delete(**kwargs)
