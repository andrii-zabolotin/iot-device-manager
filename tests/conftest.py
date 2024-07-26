from unittest.mock import MagicMock

import pytest

from src.database import db
from src.models import Device, User, Location


@pytest.fixture(scope='function')
def setup_database():
    with db:
        db.create_tables([User, Location, Device], safe=True)
    yield db
    with db:
        db.drop_tables([User, Location, Device])


@pytest.fixture
def get_location():
    return Location.create(name='Test Location')


@pytest.fixture
def get_user():
    return User.create(name='Test User', email='testuser@example.com', password='password123')
