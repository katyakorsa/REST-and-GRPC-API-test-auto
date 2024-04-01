import allure

from common_libs.db_client.db_client import DbClient


class DmDatabase:
    def __init__(
            self,
            user,
            password,
            host,
            database
    ):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        query = 'select * from "public"."Users"'
        with allure.step('Get all users'):
            dataset = self.db.send_query(query=query)

        return dataset

    def select_user_by_login(self, login: str):
        query = f'''
        select * from "public"."Users" 
        where "Login" = '{login}'
        '''
        with allure.step('Get user by login'):
            dataset = self.db.send_query(query=query)

        return dataset

    def update_user_by_login(self, login):
        query = f'''
        update "public"."Users"
        set "Activated" = true
        where "Login" = '{login}'
        '''
        with allure.step('Update user data by login'):
            dataset = self.db.send_bulk_query(query=query)

        return dataset

    def delete_user_by_login(self, login: str):
        query = f'''
        delete from "public"."Users"
        where "Login" = '{login}'
        '''
        with allure.step('Delete user by login'):
            dataset = self.db.send_bulk_query(query=query)

        return dataset
