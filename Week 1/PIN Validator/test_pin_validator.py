import pytest

from pin_validator import validate_pin

@pytest.mark.parametrize("pin, expected", [
    ("1234", True),
    ("0000", True),
    ("123", False),
    ("12345", False),
    ("12A4", False),
    ("12 4", False),
    ("", False),
    ("abcd", False),
    ("1.23", False),
    ("-123", False),
    ("9999", True),
    (" 1234", False),
    ("1234 ", False)
])

def test_validate_pin(pin, expected):
    assert validate_pin(pin) == expected