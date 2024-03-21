import structlog

from services.dm_api_account import DmApiAccount
from utils.utils import validate_account_response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    login = 'FlorenceWelch76'
    email = 'FlorenceWelch76@gmail.com'
    password = 'strong1password'

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    api.account.activate_registered_user()

    api.login.login_user(
        login=login,
        password=password,
        remember_me=True
    )

    response = api.account.change_user_email(
        login=login,
        password=password,
        email=email
    )

    validate_account_response(response=response, login=login)
