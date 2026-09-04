import pytest
from atm_withdrawal import validate_withdrawal

def test_validate_withdrawal():
    assert validate_withdrawal(100, 500, 1000) == "Withdrawal approved"

def test_invalid_amount():
    assert validate_withdrawal(-50, 500, 1000) == "Invalid amount"
    assert validate_withdrawal(0, 500, 1000) == "Invalid amount"

def test_amount_not_divisible_by_20():
    assert validate_withdrawal(25, 500, 1000) == "Amount must be divisible by 20"
    assert validate_withdrawal(30, 500, 1000) == "Amount must be divisible by 20"

def test_insufficient_funds():
    assert validate_withdrawal(600, 500, 1000) == "Insufficient funds"

def test_atm_insufficient_cash():
    assert validate_withdrawal(1000, 5000, 500) == "ATM has insufficient cash"
    assert validate_withdrawal(2000, 3000, 1500) == "ATM has insufficient cash"

def test_boundary_test():
    assert validate_withdrawal(20, 20, 20) == "Withdrawal approved"
    assert validate_withdrawal(20, 10, 20) == "Insufficient funds"
    assert validate_withdrawal(20, 30, 10) == "ATM has insufficient cash"

def test_validate_order():
    assert validate_withdrawal(550, 500, 5000) == "Amount must be divisible by 20"

