from dm_api_account.api.account_api import AccountApi
from dm_api_account.api.login_api import LoginApi


class DmApiAccount:
    def __init__(self, host, headers=None):
        self.account = AccountApi(host, headers)
        self.login = LoginApi(host, headers)
