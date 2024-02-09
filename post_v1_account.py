import requests


def post_v1_account():
    """
    Register new user
    :return:
    """

    url = "http://5.63.153.31:5051/v1/account"
    payload = {
        "login": "what44euddu334ver11",
        "email": "whate344d4uu3ver111@gmail.com",
        "password": "easypassword"
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )

    return response
