import allure
import pytest

from generic.helpers.data_generators import email_generator, full_name_generator


@allure.suite("Tests for checking PUT {host}v1/account/password")
@allure.sub_suite("Positive checks")
class TestPutV1AccountPassword:

    @pytest.mark.parametrize('login, email, password, new_password, status_code, check', [
        (full_name_generator(), email_generator(), 'strong_password', 'new_password', 201, '')
        # (full_name_generator(), email_generator(), 'strong_password', 'strong_password', 400, ''),
    ])
    @allure.title("Process of changing user password")
    def test_put_v1_account_password(
            self,
            dm_api,
            orm_db,
            login,
            email,
            password,
            new_password,
            status_code,
            check,
            assertions
    ):
        orm_db.delete_user_by_login(login=login)
        dm_api.mailhog.delete_api_v2_messages()

        assertions.check_user_was_created(login=login)
        dm_api.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )

        orm_db.update_user_by_login(login=login)
        assertions.check_user_has_activated(login=login)

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
