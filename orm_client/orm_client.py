import allure
import structlog
import uuid
from sqlalchemy import create_engine

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query is None:
            raise ValueError(f'query is missed')

        allure.attach(
            str(query),
            attachment_type=allure.attachment_type.TEXT,
            name='query'
        )
        dataset = fn(*args, **kwargs)
        if dataset is not None:
            allure.attach(
                str(dataset),
                attachment_type=allure.attachment_type.TEXT,
                name='dataset'
            )

        return dataset

    return wrapper


class OrmClient:
    def __init__(
            self,
            user,
            password,
            host,
            database,
            isolation_level='AUTOCOMMIT'
    ):
        connection_postgresql = f"postgresql://{user}:{password}@{host}/{database}"
        self.engine = create_engine(connection_postgresql, isolation_level=isolation_level)
        self.db = self.engine.connect()
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    def close_connection(self):
        """
        Close DB connection
        :return:
        """
        return self.db.close()

    @allure.attach
    def send_query(self, query):
        """
        Execute a SQL statement
        :param query:
        :return:
        """
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query)
        )
        dataset = self.db.execute(statement=query)
        result = [row for row in dataset]
        log.msg(
            event='response',
            dataset=[dict(row) for row in result]
        )
        return result

    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query)
        )
        return self.db.execute(statement=query)
