import pytest

from login_validator import validate_login


@pytest.mark.parametrize(
    "username, password, expected_output",
    [
        ("admin", "python123", "Login successful!"),
        ("admin", "wrongpassword", "Invalid password"),
        ("wronguser", "python123", "User not found"),
        ("", "python123", "Fields cannot be empty"),
        ("admin", "", "Fields cannot be empty"),
        ("", "", "Fields cannot be empty")
    ]

)

def test_validate_login(username, password, expected_output):
    assert validate_login(username, password) == expected_output
