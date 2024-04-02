import uuid

import grpc
import structlog
from google.protobuf.json_format import MessageToDict

from apis.dm_api_account_grpc.account_pb2 import RegisterAccountRequest
from apis.dm_api_account_grpc.account_pb2_grpc import AccountServiceStub

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    ]
)


def grpc_logger(func):
    def wrapper(self, request, *args, **kwargs):
        log = self.log.bind(event_id=str(uuid.uuid4()))
        method = func.__name__
        log.msg(
            event='request',
            method=method,
            channel=self.target,
            request=MessageToDict(request)
        )
        try:
            response = func(self, request, *args, **kwargs)
            log.msg(
                event='response',
                response=MessageToDict(response)
            )
            return response
        except Exception as e:
            print(f'Error {e}')
            raise

    return wrapper


class DmApiAccountGrpc:
    def __init__(self, target):
        self.target = target
        self.channel = grpc.insecure_channel(target=self.target)
        self.client = AccountServiceStub(channel=self.channel)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='grpc')

    @grpc_logger
    def register(self, request: RegisterAccountRequest):
        response = self.client.RegisterAccount(request=request)
        return response

    def close(self):
        return self.channel.close()
