balance = 1000000

while True:
    transaction_type = input("Enter transaction (debit/credit/stop): ").lower()

    if transaction_type == "stop":
        print("Transaction session ended.")
        break 

    amount = int(input("Enter the amount: "))

    if transaction_type == "debit":
        if amount <= balance:
            balance -= amount
            print("Your account is debited.")
            print("Current balance:", balance)
        else:
            print("Insufficient balance!")
    elif transaction_type == "credit":
        balance += amount
        print("Your account is credited.")
        print("Current balance:", balance)
    else:
        print("Invalid transaction type!")
