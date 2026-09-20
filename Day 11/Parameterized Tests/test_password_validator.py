import pytest
from password_validator import validate_password

@pytest.mark.parametrize(
    "password, expected",
    [
        ("python123", True),
        ("password", False),
        ("abc123", False),
        ("12345678", True),
        ("abcdefg1", True),
        ("abcdef1", False),
        ("", False),
        ("abcdefgh9", True)    
    ]
)

def test_validate_password(password, expected):
    assert validate_password(password) == expected