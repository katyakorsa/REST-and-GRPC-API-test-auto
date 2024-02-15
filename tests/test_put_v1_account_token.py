from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    token = 'a8958565-216d-4895-9f9f-0bdbf50cf9c9'
    response = api.account.put_v1_account_token(
        token=token
    )

    return response
