import requests
import structlog

from pydantic import BaseModel
from hamcrest import assert_that, has_property, has_properties, all_of, starts_with, equal_to

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def validate_request_json(json: BaseModel):
    if isinstance(json, dict):
        return json
    return json.model_dump(by_alias=True, exclude_none=True)


def validate_status_code(response: requests.Response, status_code: int):
    assert response.status_code == status_code, f'Status code must be equal {status_code}, ' \
                                                f'but it is {response.status_code}'


def validate_account_response(response, login: str):
    assert_that(response, all_of(
        has_property('resource', has_property('login', starts_with(login))),
        has_property('resource', has_properties(
            {
                'rating': has_properties(
                    {
                        'enabled': equal_to(True),
                        'quality': equal_to(0),
                        'quantity': equal_to(0)
                    }
                )
            }
        ))
    ))
