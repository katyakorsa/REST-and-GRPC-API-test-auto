from db_client.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        query = 'select * from "public"."Users"'
        dataset = self.db.send_query(query=query)

        return dataset

    def create_new_user(self):
        pass

    def get_user_by_login(self, login: str):
        query = f'''
        select * from "public"."Users" 
        where "Login" = '{login}'
        '''
        dataset = self.db.send_query(query=query)

        return dataset

    def activate_user_by_db(self, login):
        query = f'''
        update "public"."Users"
        set "Activated" = true
        where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)

        return dataset

    def delete_user_by_login(self, login: str):
        query = f'''
        delete from "public"."Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)

        return dataset
