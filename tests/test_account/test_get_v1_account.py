import allure
import pytest

from generic.assertions.response_checker import check_status_code_http
from generic.helpers.data_generators import email_generator, full_name_generator


@allure.suite("Tests for checking GET {host}v1/account")
@allure.sub_suite("Positive checks")
class TestGetV1Account:
    @pytest.mark.parametrize('login, email, password, status_code', [
        (full_name_generator(), email_generator(), 'strong_password', 201),
    ])
    @allure.title("Get all information about user")
    def test_get_v1_account(
            self,
            dm_api,
            orm_db,
            login,
            email,
            password,
            status_code,
            assertions
    ):
        orm_db.delete_user_by_login(login=login)
        dm_api.mailhog.delete_api_v2_messages()

        with check_status_code_http(expected_status_code=status_code, expected_result=check):
            dm_api.account.register_new_user(
                login=login,
                email=email,
                password=password,
                status_code=status_code
            )
        assertions.check_user_was_created(login=login)

        orm_db.update_user_by_login(login=login)
        assertions.check_user_has_activated(login=login)

        dm_api.login.login_user(
            login=login,
            password=password,
            remember_me=True
        )

        token = dm_api.login.get_auth_token(login=login, password=password)
        dm_api.account.get_current_user_info(headers=token)
