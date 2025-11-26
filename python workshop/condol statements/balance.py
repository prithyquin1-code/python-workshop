balance=10000
amount=float(input("enter the withdrawal amount:"))
if amount<=balance:
    balance -= amount
    print("your account is debited:",amount)
    print("remaining balance:",balance)
else:
    print("not sufficient balance")
