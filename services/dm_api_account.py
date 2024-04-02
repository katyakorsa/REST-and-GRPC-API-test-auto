import dm_api_account
from dm_api_account.apis import AccountApi
from dm_api_account.apis import LoginApi
from generic.helpers.account import Account
from generic.helpers.login import Login
from dm_api_account import Configuration, ApiClient


class DmApiAccount:
    def __init__(self, host, mailhog=None, headers=None):
        with dm_api_account.ApiClient(configuration=Configuration(host=host)) as api_client:
            self.account_api = AccountApi(api_client)
            self.login_api = LoginApi(api_client)
        self.mailhog = mailhog
        self.account = Account(self)
        self.login = Login(self)
