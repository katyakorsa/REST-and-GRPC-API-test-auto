import pytest

from generic.helpers.checkers import validate_account_response, asserts
from utils.data_generators import email_generator, full_name_generator


@pytest.mark.parametrize('login, email, password, new_password, status_code, check', [
    (full_name_generator(), email_generator(), 'strong_password', 'new_password', 201, '')
    # (full_name_generator(), email_generator(), 'strong_password', 'strong_password', 400, ''),
])
def test_put_v1_account_password(
        dm_api,
        dm_orm,
        login,
        email,
        password,
        new_password,
        status_code,
        check
):
    dm_orm.delete_user_by_login(login=login)
    dm_api.mailhog.delete_api_v2_messages()

    dm_api.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    dm_orm.update_user_by_login(login=login)
    dataset = dm_orm.select_user_by_login(login=login)
    for row in dataset:
        asserts(row=row, login=login, activate_flag=True)

    dm_api.login.login_user(
        login=login,
        password=password,
        remember_me=True
    )

    headers = dm_api.login.get_auth_token(login=login, password=password)

    dm_api.account.reset_user_password(
        login=login,
        email=email
    )

    dm_api.account.change_user_password(
        login=login,
        old_password=password,
        new_password=new_password,
        headers=headers
    )
