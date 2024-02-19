import requests.exceptions
import structlog
import curlify
import uuid

from requests import session, Response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class RestClient:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()

        if headers:
            self.session.headers.update(headers)

        self.log = structlog.get_logger(self.__class__.__name__).bind(service='apis')

    def post(self, url: str, **kwargs) -> Response:
        return self._send_request('POST', url, **kwargs)

    def put(self, url: str, **kwargs) -> Response:
        return self._send_request('PUT', url, **kwargs)

    def get(self, url: str, **kwargs) -> Response:
        return self._send_request('GET', url, **kwargs)

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
