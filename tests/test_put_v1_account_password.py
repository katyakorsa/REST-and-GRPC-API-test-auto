import structlog
from services.dm_api_account import DmApiAccount
from utils.utils import validate_account_response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    login = 'FlorenceWelch77'
    email = 'FlorenceWelch77@gmail.com'
    password = 'strong1password'
    new_password = 'newpassword'

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

    headers = api.login.get_auth_token(login=login, password=password)

    api.account.reset_user_password(
        login=login,
        email=email
    )
    reset_token = api.mailhog.get_reset_token(login=login)

    response = api.account.change_user_password(
        login=login,
        token=reset_token,
        old_password=password,
        new_password=new_password,
        headers=headers
    )

    validate_account_response(response=response, login=login)
