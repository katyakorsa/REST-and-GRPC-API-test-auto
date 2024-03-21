import structlog
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    login = 'FlorenceWelch80'
    email = 'FlorenceWelch80@gmail.com'
    password = 'stringstring'

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

    token = api.login.get_auth_token(login=login, password=password)
    api.account.get_current_user_info(headers=token)
