import structlog
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_delete_v1_account_login():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    login = 'FlorenceWelch68'
    email = 'FlorenceWelch68@gmail.com'
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

    headers = api.login.get_auth_token(
        login=login,
        password=password
    )

    api.login.logout_from_every_device(headers=headers)
