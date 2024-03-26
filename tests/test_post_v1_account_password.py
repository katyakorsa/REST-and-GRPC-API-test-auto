import structlog

from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    db_path = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')

    login = 'FlorenceWelch74'
    email = 'FlorenceWelch74@gmail.com'
    password = 'strong1password'

    db_path.delete_user_by_login(login=login)
    dataset = db_path.select_user_by_login(login=login)
    assert len(dataset) == 0

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dataset = db_path.select_user_by_login(login=login)
    for row in dataset:
        assert row.Login == login, f'The user {login} is not registered'
        assert row.Activated is False, f'The user {login} has already been activated'

    db_path.update_user_by_login(login=login)

    dataset = db_path.select_user_by_login(login=login)
    for row in dataset:
        assert row.Activated is True, f'The user {login} is not activated'

    api.login.login_user(
        login=login,
        password=password,
        remember_me=True
    )

    api.account.reset_user_password(
        login=login,
        email=email
    )
