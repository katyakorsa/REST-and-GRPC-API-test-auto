import requests


def put_v1_account_token():
    """
    Activate registered user
    :return:
    """
    token = "0045fb15-b7b2-47a1-b04b-278d488585c1"
    url = f"http://5.63.153.31:5051/v1/account/{token}"
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers
    )

    return response
