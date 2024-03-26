from typing import List
from sqlalchemy import select, delete, update
from orm_client.orm_client import OrmClient
from models.orm_models.user_model import User


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.orm_db = OrmClient(user, password, host, database)

    def select_all_users(self):
        query = select(User)
        dataset = self.orm_db.send_query(query=query)

        return dataset

    def select_user_by_login(self, login: str) -> List[User]:
        query = select(User).where(
            User.Login == login
        )
        dataset = self.orm_db.send_query(query)

        return dataset

    def delete_user_by_login(self, login: str):
        query = delete(User).where(
            User.Login == login
        )
        dataset = self.orm_db.send_bulk_query(query=query)

        return dataset

    def update_user_by_login(self, login: str):
        query = update(User).where(
            User.Login == login
        ).values(Activated=True)
        dataset = self.orm_db.send_bulk_query(query=query)

        return dataset

    def create_new_user(self):
        pass