from apis.dm_api_account.models import LoginCredentials


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
    ):
        response = self.dm_api_account.login_api.post_v1_account_login(
            json=LoginCredentials(
                login=login,
                password=password,
                rememberMe=remember_me
            )
        )

        return response

    def get_auth_token(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        response = self.login_user(login=login, password=password, remember_me=remember_me)
        token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}

        return token

    def logout_user(self, **kwargs):
        response = self.dm_api_account.login_api.delete_v1_account_login(**kwargs)

        return response

    def logout_from_every_device(self, **kwargs):
        response = self.dm_api_account.login_api.delete_v1_account_login_all(**kwargs)

        return response
