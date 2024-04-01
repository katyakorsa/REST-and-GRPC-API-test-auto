import json

import requests.exceptions
import structlog
import curlify
import uuid
import allure

from requests import session, Response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        body = kwargs.get('json')
        if body:
            allure.attach(
                json.dumps(kwargs.get('json'), indent=2),
                attachment_type=allure.attachment_type.JSON,
                name='request'
            )
        response = fn(*args, **kwargs)
        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            response_text = response.text
            status_code = f'status_code: {response.status_code}'
            allure.attach(
                response_text if len(response_text) > 0 else status_code,
                attachment_type=allure.attachment_type.TEXT,
                name='response'
            )
        else:
            allure.attach(
                json.dumps(response_json, indent=2),
                attachment_type=allure.attachment_type.JSON,
                name='response'
            )
        return response

    return wrapper


class RestClient:

    def __init__(self, host: str, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

        self.log = structlog.get_logger(self.__class__.__name__).bind(service='apis')

    @allure_attach
    def post(self, url: str, **kwargs) -> Response:
        return self._send_request('POST', url, **kwargs)

    @allure_attach
    def put(self, url: str, **kwargs) -> Response:
        return self._send_request('PUT', url, **kwargs)

    @allure_attach
    def get(self, url: str, **kwargs) -> Response:
        return self._send_request('GET', url, **kwargs)

    @allure_attach
    def delete(self, url: str, **kwargs) -> Response:
        return self._send_request('DELETE', url, **kwargs)

    def _send_request(self, method, url, **kwargs) -> Response:
        merged_url = self.host + url
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            method=method,
            merged_url=merged_url,
            params=kwargs.get('params'),
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data')
        )
        response = self.session.request(
            method=method,
            url=merged_url,
            **kwargs
        )
        curl = curlify.to_curl(response.request)
        allure.attach(
            curl,
            attachment_type=allure.attachment_type.TEXT,
            name='curl'
        )
        log.msg(
            event='response',
            status_code=response.status_code,
            headers=response.headers,
            json=self._get_json(response),
            text=response.text,
            content=response.content,
            curl=curl
        )

        return response

    @staticmethod
    def _get_json(response):
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return
