import time

from services.dm_api_account import DmApiAccount
from tests import test_put_v1_account_token
from dm_api_account.models.registration_model import Registration


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    response = api.account.post_v1_account(
        json=Registration(
            login='mailo_the_dog1',
            email='mailo_the_dog1@wolt.com',
            password='stringstring'
        )
    )

    # activating an account
    time.sleep(2)
    test_put_v1_account_token.test_put_v1_account_token()
