import pytest
import structlog

from collections import namedtuple
from generic.helpers.dm_db import DmDatabase
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.mailhog import MailhogApi
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def mailhog():
    return MailhogApi(host='http://5.63.153.31:5025')


@pytest.fixture
def dm_api(mailhog):
    return DmApiAccount(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture
def dm_db():
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    return db


@pytest.fixture
def dm_orm():
    db = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    return db


@pytest.fixture
def prepare_user(dm_api, dm_db):
    user = namedtuple('User', 'login, email, password')
    User = user(login='Olivia Rose', email='OliviaRose@gmail.com', password='strong!password')
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0

    return User
