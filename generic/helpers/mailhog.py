import json
import time

from requests import Response
from rest_client.rest_client import RestClient


# reuse later
# def retry(fn):
#     def wrapper(*args, **kwargs):
#         for _ in range(5):
#             response = fn(*args, **kwargs)
#             emails = response.json()['items']
#             if len(emails) < 5:
#                 continue
#             else:
#                 return response
#
#     return wrapper()


class MailhogApi:

    def __init__(self, host='http://5.63.153.31:5025'):
        self.host = host
        self.client = RestClient(host=host)

    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages with a set limit
        :return:
        """

        response = self.client.get(
            url=f"/api/v2/messages",
            params={
                'limit': limit
            }
        )

        return response

    def delete_api_v2_messages(self) -> Response:
        """
        Delete all messages
        :return:
        """
        response = self.client.delete(
            url=f"/api/v1/messages"
        )

        return response

    def get_token_from_last_email(self) -> str:
        """
        Get an activation token from the latest email
        :return:
        """

        email = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(email['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]

        return token

    def get_token_by_login(self, login: str, attempt: int = 50):
        """
        Get an activation token by login
        :param login:
        :param attempt:
        :return:
        """

        if attempt == 0:
            raise AssertionError(f'Failed to receive the email with login {login}')
        emails = self.get_api_v2_messages(limit=100).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]

                return token

        time.sleep(2)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def get_reset_token(self, login: str):
        """
        Get token from email to reset the password
        :param login:
        :return:
        """

        emails = self.get_api_v2_messages(limit=10).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                reset_token = user_data['ConfirmationLinkUri'].split('/')[-1]

                return reset_token

    def delete_message_by_token(self, token: str):
        # дополнить позже
        """
        Delete a specific message by token
        :param token:
        :return:
        """
        response = self.client.delete(
            url=f"/api/v1/messages/{token}=@mailhog.example"
        )

        return response
