import requests


def delete_v1_account_login_all():
    """
    Logout from every device
    :return:
    """

    url = "http://5.63.153.31:5051/v1/account/login/all"
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5AcSwYTQAwc5mFIZGYQKN/OhoaK2TsCP7LFSPtjfaEInvZkT9IOMY0oKgzYiTq0cHSUiJA+bFfRdjCvCiT'
                           'P9Pj9yh6Id2DjvHH6C5Ufn5olGMMOHlNCnCQBUK0kBszF14c=',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="DELETE",
        url=url,
        headers=headers
    )

    return response
