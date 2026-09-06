from bank_account import BankAccount

def test_create_account():
    account = BankAccount("Alice", 1000)
    assert account.owner == "Alice", f"Expected owner to be Alice but got {account.owner}"
    assert account.balance == 1000, f"Expected balance to be 1000 but got {account.balance}"

def test_deposit():
    account = BankAccount("Bob", 500)
    account.deposit(200)
    assert account.balance == 700, f"Expected balance to be 700 but got {account.balance}"

def test_withdraw():
    account = BankAccount("Charlie", 800)
    account.withdraw(300)
    assert account.balance == 500, f"Expected balance to be 500 but got {account.balance}"

def test_withdraw_insufficient_funds():
    account = BankAccount("David", 400)
    account.withdraw(500)
    assert account.balance == 400, f"Expected balance to remain 400 but got {account.balance}"

def test_transaction_history():
    account = BankAccount("Eve", 600)
    account.history("Deposit: 200")
    account.history("Withdraw: 100")
    assert account.transaction == ["Deposit: 200", "Withdraw: 100"], f"Expected transaction history to be ['Deposit: 200', 'Withdraw: 100'] but got {account.transaction}"