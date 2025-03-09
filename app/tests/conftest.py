import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def test_user_for_register():
    return {
        'username': 'Egor'
    }

@pytest.fixture
def test_user_for_create_article():
    return {
        'username':'Egor',
        'title':'cms',
        'description':'Today i will make cms system',
    }

@pytest.fixture
def test_user_for_update_article():
    return {
        'username':'Egor',
        'title': 'update cms',
        'description': 'I make updatr cms system'
    }

@pytest.fixture(scope='function')
def session():
    engine = create_engine()