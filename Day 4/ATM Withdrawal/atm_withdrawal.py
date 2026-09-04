def validate_withdrawal(amount, balance, atm_cash):
    if amount <= 0:
        return "Invalid amount"
    if amount % 20 != 0:
        return "Amount must be divisible by 20"
    if amount > balance:
        return "Insufficient funds"
    if amount > atm_cash:
        return "ATM has insufficient cash"
    else:
        return "Withdrawal approved"

