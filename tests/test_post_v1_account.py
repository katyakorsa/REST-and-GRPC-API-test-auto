import time

from services.dm_api_account import DmApiAccount
from tests import test_put_v1_account_token
from dm_api_account.models.registration_model import RegistrationModel


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    response = api.account.post_v1_account(
        json=RegistrationModel(
            login='berry_lemonade11',
            email='berry_lemonade11@wolt.com',
            password='stringstring'
        )
    )
    assert response.status_code == 201, f'The response status code must be equal 201, but it is {response.status_code}'

    # activating an account
    time.sleep(2)
    test_put_v1_account_token.test_put_v1_account_token()
