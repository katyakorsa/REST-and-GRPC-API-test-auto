import time

from dm_api_account.models.change_email_model import ChangeEmailModel
from dm_api_account.models.registration_model import RegistrationModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_email():
    # used hosts
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    api.account.post_v1_account(
        json=RegistrationModel(
            login='berry_lemonade14',
            email='berry_lemonade14@wolt.com',
            password='stringstring'
        )
    )

    # activation an account
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(
        token=token
    )

    # changing an email of existing user
    response = api.account.put_v1_account_email(
        json=ChangeEmailModel(
            login='berry_lemonade14',
            password='stringstring',
            email='berry_lemonade14@wolt.ru'
        )
    )
    assert response.status_code == 200, f'The response status code must be equal 200, but it is {response.status_code}'
