balance = 1000000
type = input("Enter transaction (debit/credit): ")
amount = int(input("Enter the amount: "))
if type == "debit":
    if amount <= balance:
        balance -= amount
        print("your account is debited")
        print("current balance:", balance)
    else:
        print("Insufficient balance!")
elif type == "credit":
    balance += amount
    print("Your account is credited")
    print("current balance:", balance)
else:
    print("insufficient")


