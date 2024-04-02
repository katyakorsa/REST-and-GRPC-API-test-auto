from apis.dm_api_account_grpc.account_pb2 import RegisterAccountRequest
from apis.dm_api_account_grpc_async.dm_api_account_grpc_async import DmApiAccountGrpcAsync


class AccountGrpcAsync:
    def __init__(self, host, port):
        self.grpc_account = DmApiAccountGrpcAsync(host=host, port=port)

    async def account_registration(self, login: str, email: str, password: str):
        response = await self.grpc_account.register_account(
            request=RegisterAccountRequest(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def close(self):
        return self.grpc_account.close()
