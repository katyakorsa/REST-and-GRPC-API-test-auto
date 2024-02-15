from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "maltesers_disco",
        "email": "maltesers_disco@yandex.ru",
        "password": "strongpass30!"
    }
    response = api.account.post_v1_account(
        json=json
    )

    return response
