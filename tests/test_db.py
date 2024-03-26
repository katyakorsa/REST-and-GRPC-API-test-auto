import structlog

from generic.helpers.orm_db import OrmDatabase

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class TestClass:

    def test_select_all_users(self):
        user = 'postgres'
        password = 'admin'
        host = '5.63.153.31'
        database = 'dm3.5'
        orm = OrmDatabase(user=user, password=password, host=host, database=database)

        dataset = orm.select_all_users()
        print(dataset)

    def test_select_user_by_login(self):
        user = 'postgres'
        password = 'admin'
        host = '5.63.153.31'
        database = 'dm3.5'
        orm = OrmDatabase(user=user, password=password, host=host, database=database)

        dataset = orm.select_user_by_login(login='FlorenceWelch11')
        # print(dataset)

        orm.orm_db.close_connection()
