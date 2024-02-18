import json

from requests import Response
from rest_client.rest_client import RestClient


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

    def get_token_from_last_email(self) -> str:
        """
        Get an activation token from the latest email
        :return:
        """

        email = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(email['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]

        return token
