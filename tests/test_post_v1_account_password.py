import structlog

from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    login = 'FlorenceWelch74'
    email = 'FlorenceWelch74@gmail.com'
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

    api.account.reset_user_password(
        login=login,
        email=email
    )
