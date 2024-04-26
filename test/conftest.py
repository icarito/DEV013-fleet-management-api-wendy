"""Client configuration"""
import pytest
from src.app import app

@pytest.fixture
def client():
    """Client definition"""
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client