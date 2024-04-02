import allure
import pytest

from generic.helpers.data_generators import email_generator, full_name_generator


@allure.suite("Tests for checking PUT {host}v1/account/email")
@allure.sub_suite("Positive checks")
class TestPutV1AccountEmail:
    @pytest.mark.parametrize('login, email, password, status_code', [
        (full_name_generator(), email_generator(), 'strong_password', 201),
    ])
    @allure.title("Process of changing user email")
    def test_put_v1_account_email(
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

        dm_api.account.register_new_user(
            login=login,
            email=email,
            password=password
        )
        assertions.check_user_was_created(login=login)

        orm_db.update_user_by_login(login=login)
        assertions.check_user_has_activated(login=login)

        dm_api.login.login_user(
            login=login,
            password=password,
            remember_me=True
        )

        dm_api.account.change_user_email(
            login=login,
            password=password,
            email=email
        )
