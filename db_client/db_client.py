import uuid

import records
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class DbClient:
    def __init__(self, user, password, host, database):
        connection_postgresql = f"postgresql://{user}:{password}@{host}/{database}"
        self.db = records.Database(connection_postgresql, isolation_level='AUTOCOMMIT')
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

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

    def send_bulk_query(self, query):
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        self.db.bulk_query(query=query)
