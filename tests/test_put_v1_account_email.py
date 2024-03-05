import time

from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from utils.helpers import validate_account_response


def test_put_v1_account_email():
    # used hosts
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    api.account.post_v1_account(
        json=Registration(
            login='mailo_funny_dog',
            email='mailo_funny_dog@wolt.com',
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
        json=ChangeEmail(
            login='mailo_funny_dog',
            password='stringstring',
            email='mailo_funny_dog@wolt.ru'
        )
    )

    validate_account_response(response=response, login='mailo_funny_dog')
