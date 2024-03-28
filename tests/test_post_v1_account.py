import pytest
from hamcrest import assert_that, has_entries

from generic.helpers.checkers import asserts
from utils.data_generators import random_string, email_generator, full_name_generator


@pytest.mark.parametrize('login, email, password, status_code, check', [
    (full_name_generator(), email_generator(), 'strong_password', 201, ''),
    (full_name_generator(), email_generator(), random_string(1, 5), 400, {"Password": ["Short"]}),
    ('а', email_generator(), 'strong_password', 400, {"Login": ["Short"]}),
    ('а', 'florence_welch@', 'strong_password', 400, {"Email": ["Invalid"]}),
    ('а', 'florence.gmail.com', 'strong_password', 400, {"Email": ["Invalid"]})
])
def test_post_v1_account(
        dm_api,
        dm_db,
        login,
        email,
        password,
        status_code,
        check
):
    dm_db.delete_user_by_login(login=login)
    dm_api.mailhog.delete_api_v2_messages()

    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        asserts(row=row, login=login, activate_flag=False)

    response = dm_api.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )

    if status_code == 201:
        dm_db.activate_user_by_db(login=login)
        dataset = dm_db.get_user_by_login(login=login)
        for row in dataset:
            asserts(row=row, login=login, activate_flag=True)
    else:
        error_message = response.json()['errors']
        assert_that(error_message, has_entries(check))

    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        asserts(row=row, login=login, activate_flag=True)
