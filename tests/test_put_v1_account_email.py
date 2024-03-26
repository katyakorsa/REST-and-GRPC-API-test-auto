import structlog

from services.dm_api_account import DmApiAccount
from generic.helpers.orm_db import OrmDatabase
from utils.utils import validate_account_response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    db_path = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')

    login = 'Apple Welch'
    email = 'apple_welch@gmail.com'
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

    # добавить позже изменение логина через БД
    response = api.account.change_user_email(
        login=login,
        password=password,
        email=email
    )

    validate_account_response(response=response, login=login)
