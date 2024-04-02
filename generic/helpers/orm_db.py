from typing import List

import allure
from sqlalchemy import select, delete, update
from orm_client.orm_client import OrmClient
from generic.helpers.orm_models.user_model import User


class OrmDatabase:
    def __init__(
            self,
            user,
            password,
            host,
            database
    ):
        self.orm = OrmClient(user, password, host, database)

    def select_all_users(self):
        with allure.step('Get all users'):
            query = select(User)

        return self.orm.send_query(query=query)

    def select_user_by_login(self, login: str) -> List[User]:
        with allure.step('Get entity by login'):
            query = select(User).where(
                User.Login == login
            )

        return self.orm.send_query(query=query)

    def delete_user_by_login(self, login: str):
        with allure.step('Delete particular user by login'):
            query = delete(User).where(
                User.Login == login
            )

        return self.orm.send_bulk_query(query=query)

    def update_user_by_login(self, login: str):
        with allure.step('Update user data by login'):
            query = update(User).where(
                User.Login == login
            ).values(dict(Activated=True))

        return self.orm.send_bulk_query(query=query)
