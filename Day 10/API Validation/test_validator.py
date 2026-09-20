from validator import validate_user

def test_valid_user():
    user = {
        "id": 1,
        "name": "Asaf",
        "email": "asaf@example.com"
    }

    assert validate_user(user) == True

def test_user_missing_email():
    user = {
        "id": 1,
        "name": "Asaf"
    }

    assert validate_user(user) == False

def test_user_missing_name():
    user = {
        "id": 1,
        "email": "asaf@example.com"
    }

    assert validate_user(user) == False

def test_user_invalid_id_type():
    user = {
        "id": "1",
        "name": "Asaf",
        "email": "asaf@example.com"
    }

    assert validate_user(user) == False

def test_user_invalid_email():
    user = {
        "id": 1,
        "name": "Asaf",
        "email": "this-is-not-an-email"
    }

    assert validate_user(user) == False