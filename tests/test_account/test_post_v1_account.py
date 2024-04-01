import allure
import pytest
from hamcrest import assert_that, has_entries

from generic.helpers.data_generators import random_string, email_generator, full_name_generator


@allure.suite("Tests for checking POST {host}v1/account")
@allure.sub_suite("Positive and negative checks")
class TestPostV1Account:
    @pytest.mark.parametrize('login, email, password, status_code, check', [
        (full_name_generator(), email_generator(), 'strong_password', 201, ''),
        (full_name_generator(), email_generator(), random_string(1, 5), 400, {"Password": ["Short"]}),
        ('а', email_generator(), 'strong_password', 400, {"Login": ["Short"]}),
        ('а', 'florence_welch@', 'strong_password', 400, {"Email": ["Invalid"]}),
        ('а', 'florence.gmail.com', 'strong_password', 400, {"Email": ["Invalid"]})
    ])
    @allure.title("Verification of user creation")
    def test_post_v1_account(
            self,
            dm_api,
            dm_db,
            login,
            email,
            password,
            status_code,
            check,
            assertions
    ):
        """
        Test verification of user creation and activation in the database
        """

        dm_db.delete_user_by_login(login=login)
        dm_api.mailhog.delete_api_v2_messages()

        response = dm_api.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )

        assertions.check_user_was_created(login=login)

        if status_code == 201:
            dm_db.update_user_by_login(login=login)
            assertions.check_user_has_activated(login=login)
        else:
            error_message = response.json()['errors']
            assert_that(error_message, has_entries(check))
