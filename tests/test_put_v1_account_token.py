import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.registration_model import RegistrationModel


def test_put_v1_account_token():
    # used hosts
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    api.account.post_v1_account(
        json=RegistrationModel(
            login='berry_lemonade15',
            email='berry_lemonade15@wolt.com',
            password='stringstring'
        )
    )

    # activation an account
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(
        token=token
    )

    assert response.status_code == 200, f'The response status code must be equal 200, but it is {response.status_code}'
