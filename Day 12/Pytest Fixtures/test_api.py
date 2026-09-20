import pytest
from api_client import get_user

@pytest.fixture
def user_response():
    response = get_user(1)
    return response

@pytest.fixture
def user_data(user_response):
    return user_response.json()

def test_user_status_code(user_response):
    assert user_response.status_code == 200


def test_user_data(user_data):
    assert user_data["id"] == 1
    assert user_data["name"] == "Leanne Graham"
    assert user_data["email"] == "Sincere@april.biz"

def test_user_address(user_data):
    assert user_data["address"]["street"] == "Kulas Light"
    assert user_data["address"]["city"] == "Gwenborough"