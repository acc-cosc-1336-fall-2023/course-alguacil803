import bank_account

account = bank_account.BankAccount(50)

print(account.get_balance())

amount = int(input("Enter deposit amount: "))

account.deposit(amount)
My_atm.make_deposit

print(account.get_balance())

amount = int(input("Enter amount: "))

account.withdraw(amount)

print(account.get_balance())