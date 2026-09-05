prices = []

def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

total_price = calculate_total(prices)

def calculate_discounted_total(prices, discount):
    total = calculate_total(prices)
    discounted_total = total - (total * discount)
    return discounted_total
