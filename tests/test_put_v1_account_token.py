import pytest

from generic.helpers.checkers import asserts
from utils.data_generators import email_generator, full_name_generator


@pytest.mark.parametrize('login, email, password, status_code', [
    (full_name_generator(), email_generator(), 'strong_password', 201)
])
def test_put_v1_account_token(
        dm_api,
        dm_orm,
        login,
        email,
        password,
        status_code
):
    dm_orm.delete_user_by_login(login=login)
    dm_api.mailhog.delete_api_v2_messages()

    dm_api.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    dataset = dm_orm.select_user_by_login(login=login)
    for row in dataset:
        asserts(row=row, login=login, activate_flag=False)

    dm_orm.update_user_by_login(login=login)

    dataset = dm_orm.select_user_by_login(login=login)
    for row in dataset:
        asserts(row=row, login=login, activate_flag=True)
