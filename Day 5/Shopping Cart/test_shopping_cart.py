from shopping_cart import calculate_total
from shopping_cart import calculate_discounted_total

def test_multiple_products():
    prices = [43, 12, 4]
    total = calculate_total(prices)
    assert total == 59, f"Expected 59 but got {total}"

def test_one_product():
    prices = [20]
    total = calculate_total(prices)
    assert total == 20, f"Expected 20 but got {total}"

def test_empty_cart():
    prices = []
    total = calculate_total(prices)
    assert total == 0, f"Expected 0 but got {total}"

def test_larger_cart():
    prices = [100, 200, 300, 400]
    total = calculate_total(prices)
    assert total == 1000, f"Expected 1000 but got {total}"

def test_discount_20():
    prices = [100, 200, 300]
    discount = 0.2
    discounted_total = calculate_discounted_total(prices, discount)
    assert discounted_total == 480, f"Expected 480 but got {discounted_total}"

def test_discount_50():
    prices = [100, 200, 300]
    discount = 0.5
    discounted_total = calculate_discounted_total(prices, discount)
    assert discounted_total == 300, f"Expected 300 but got {discounted_total}"

def test_discount_0():
    prices = [100, 200, 300]
    discount = 0.0
    discounted_total = calculate_discounted_total(prices, discount)
    assert discounted_total == 600, f"Expected 600 but got {discounted_total}"