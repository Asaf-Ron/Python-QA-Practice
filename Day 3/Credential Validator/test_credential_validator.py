from credential_validator import validatade_credentials

def test_username_required():
    assert validatade_credentials("", "password123") == "Username is required"

def test_username_too_short():
    assert validatade_credentials("abc", "password123") == "Username is too short"

def test_password_required():
    assert validatade_credentials("Asaf", "") == "Password is required"

def test_password_too_short():
    assert validatade_credentials("Asaf", "python") == "Password is too short"

def test_password_no_digit():
    assert validatade_credentials("Asaf", "password") == "Password must contain at least one digit"

def test_valid_credentials():
    assert validatade_credentials("Asaf", "password1234") == "Login valid!"