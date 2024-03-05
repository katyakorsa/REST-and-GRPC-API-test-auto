import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from utils.helpers import validate_account_response
from dm_api_account.models.registration_model import Registration


def test_put_v1_account_token():
    # used hosts
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # creating an account
    api.account.post_v1_account(
        json=Registration(
            login='pear_rosemary13',
            email='pear_rosemary13@wolt.com',
            password='stringstring'
        )
    )

    # activation an account
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(
        token=token
    )

    validate_account_response(response=response, login='pear_rosemary13')
