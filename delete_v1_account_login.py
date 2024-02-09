import requests


def delete_v1_account_login():
    """
    Logout as current user
    :return:
    """

    url = "http://5.63.153.31:5051/v1/account/login"
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5AcSwYTQAwc5mFIZGYQKN/OhoaK2TsCP7LFSPtjfaEInvZkT9IOMY0oKgzYiTq0cHSUiJA+bFfRdjCvC'
                           'iTP9Pj9yh6Id2DjvHH6C5Ufn5olGMMOHlNCnCQBUK0kBszF14c=',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="DELETE",
        url=url,
        headers=headers
    )

    return response
