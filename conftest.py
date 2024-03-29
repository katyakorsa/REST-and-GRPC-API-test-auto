import pytest
import structlog

from collections import namedtuple
from pathlib import Path
from vyper import v

from generic.helpers.dm_db import DmDatabase
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.mailhog import MailhogApi
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    ]
)

options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5.host'
)


@pytest.fixture
def mailhog():
    return MailhogApi(
        host=v.get('service.mailhog')
    )


@pytest.fixture
def dm_api(mailhog):
    return DmApiAccount(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )


@pytest.fixture
def dm_db():
    db = DmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    return db


@pytest.fixture
def dm_orm():
    db = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    return db


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='staging'
    )
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)


@pytest.fixture
def prepare_user(dm_api, dm_db):
    user = namedtuple(
        'User',
        'login, email, password'
    )
    User = user(
        login='Olivia Rose',
        email='OliviaRose@gmail.com',
        password='strong!password'
    )
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0

    return User
