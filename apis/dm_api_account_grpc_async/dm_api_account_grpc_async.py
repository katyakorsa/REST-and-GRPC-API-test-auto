import structlog
from grpclib.client import Channel

from apis.dm_api_account_grpc_async import AccountServiceStub, RegisterAccountRequest


class DmApiAccountGrpcAsync:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.channel = Channel(host=host, port=port)
        self.client = AccountServiceStub(channel=self.channel)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='grpc')

    async def register_account(self, request: RegisterAccountRequest):
        return await self.client.register_account(
            register_account_request=request
        )

    def close(self):
        self.channel.close()
