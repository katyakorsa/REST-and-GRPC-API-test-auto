import uuid

import allure
import records
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query:
            allure.attach(
                str(query),
                attachment_type=allure.attachment_type.TEXT,
                name='query'
            )
        result = fn(*args, **kwargs)
        return result

    return wrapper


class DbClient:
    def __init__(self, user, password, host, database):
        connection_postgresql = f"postgresql://{user}:{password}@{host}/{database}"
        self.db = records.Database(connection_postgresql, isolation_level='AUTOCOMMIT')
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    @allure_attach
    def send_query(self, query):
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        dataset = self.db.query(query=query).as_dict()
        log.msg(
            event='response',
            dataset=dataset
        )

        return dataset

    @allure_attach
    def send_bulk_query(self, query):
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        self.db.bulk_query(query=query)
