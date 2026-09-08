from api_client import get_user, get_user_data

def test_get_existing_user():
    status_code, user = get_user(1)
    assert status_code == 200
    assert user["id"] == 1

def test_user_has_email():
    status_code, user = get_user(1)
    assert status_code == 200
    assert user["email"] != ""

def test_get_different_user():
    status_code, user = get_user(2)
    assert status_code == 200
    assert user["id"] == 2

def test_user_not_found():
    status_code, user = get_user(999)
    assert status_code == 404
    assert user == {}

def test_user_data():
    data = get_user_data(1)
    assert isinstance(data, dict)
    assert data["id"] == 1