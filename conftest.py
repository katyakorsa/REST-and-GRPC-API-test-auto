import pytest
import structlog

from collections import namedtuple
from pathlib import Path
from vyper import v

from data.post_v1_account import PostV1AccountData as user_data
from generic.assertions.post_v1_account import AssertionsPostV1Account
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
def orm_db():
    db = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    yield db
    db.orm.close_connection()


connect = None


@pytest.fixture
def dm_db():
    global connect
    if connect is None:
        connect = DmDatabase(
            user=v.get('database.dm3_5.user'),
            password=v.get('database.dm3_5.password'),
            host=v.get('database.dm3_5.host'),
            database=v.get('database.dm3_5.database')
        )
    yield connect
    # connect.db.db.close()


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
        login=user_data.login,
        email=user_data.email,
        password=user_data.password
    )
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.select_user_by_login(login=User.login)
    assert len(dataset) == 0

    return User


@pytest.fixture
def assertions(dm_db):
    return AssertionsPostV1Account(dm_db)
