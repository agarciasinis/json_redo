import pytest

from unittest.mock import patch
from exercise.customer.models import Customer


@pytest.fixture
def customer():
    return Customer(name='James Baker',
                    email='gabriellazamora@example.org',
                    phone='+1-089-080-9224x470',
                    url='https://esparza-alvarez.com/',
                    type='post')


@pytest.fixture
def mock_send_sms():
    with patch('exercise.core.notifications.send_sms') as mock:
        yield mock


@pytest.fixture
def mock_send_email():
    with patch('exercise.core.notifications.send_email') as mock:
        yield mock


@pytest.fixture
def mock_send_post():
    with patch('exercise.core.notifications.send_post') as mock:
        yield mock
