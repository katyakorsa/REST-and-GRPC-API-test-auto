import time

from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from utils.helpers import validate_account_response


def test_post_v1_account_login():
    # used hosts
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    api.account.post_v1_account(
        json=Registration(
            login='pear_rosemary5',
            email='pear_rosemary5@wolt.com',
            password='stringstring'
        )
    )

    # activation an account
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(
        token=token
    )

    # login via credentials
    response = api.login.post_v1_account_login(
        json=LoginCredentials(
            login='pear_rosemary5',
            password='stringstring',
            rememberMe=True
        )
    )

    validate_account_response(response=response, login='pear_rosemary5')
