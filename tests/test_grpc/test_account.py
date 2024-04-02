import pytest
import pytest_asyncio

from apis.dm_api_account_grpc_async import RegisterAccountRequest


def test_register_grpc(grpc_account):
    response = grpc_account.account_registration(
        login='test_grpc7',
        email='test_grpc7@gmail.com',
        password='strong_password'
    )
    print(response)


@pytest.mark.asyncio
async def test_register_grpc_async(grpc_account_async):
    response = await grpc_account_async.account_registration(
        login='test_grpc7',
        email='test_grpc7@gmail.com',
        password='strong_password'
    )
    print(response)
