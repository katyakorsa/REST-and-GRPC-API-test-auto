import allure
import pytest

from hamcrest import assert_that, has_entries

from generic.assertions.response_checker import check_status_code_http
from generic.helpers.data_generators import email_generator, random_string, full_name_generator


@allure.suite("Tests for checking POST {host}v1/account/login")
@allure.sub_suite("Positive checks")
class TestPostV1AccountLogin:

    @pytest.mark.parametrize('login, email, password, status_code, check', [
        (full_name_generator(), email_generator(), 'strong_password', 201, ''),
        (full_name_generator(), email_generator(), random_string(1, 5), 400, {"Password": ["Short"]}),
        ('а', email_generator(), 'strong_password', 400, {"Login": ["Short"]}),
        ('а', 'florence_welch@', 'strong_password', 400, {"Email": ["Invalid"]}),
        ('а', 'florence.gmail.com', 'strong_password', 400, {"Email": ["Invalid"]})
    ])
    @allure.title("Process of user authorization")
    def test_post_v1_account_login(
            self,
            dm_api,
            orm_db,
            login,
            email,
            password,
            status_code,
            check,
            assertions
    ):
        orm_db.delete_user_by_login(login=login)
        dm_api.mailhog.delete_api_v2_messages()

        with check_status_code_http(expected_status_code=status_code, expected_result=check):
            dm_api.account.register_new_user(
                login=login,
                email=email,
                password=password
            )

        if status_code == 201:
            assertions.check_user_was_created(login=login)
            orm_db.update_user_by_login(login=login)
            assertions.check_user_has_activated(login=login)
            dm_api.login.login_user(
                login=login,
                password=password,
                remember_me=True
            )
