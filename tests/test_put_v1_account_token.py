import structlog

from services.dm_api_account import DmApiAccount
from utils.utils import validate_account_response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    login = 'FlorenceWelch78'
    email = 'FlorenceWelch78@gmail.com'
    password = 'strong1password'

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    response = api.account.activate_registered_user()

    validate_account_response(response=response, login=login)

