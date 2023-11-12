import bank_account, atm, menu

account = bank_account.BankAccount(50)

my_atm = atm.ATM(bank_account)

print(account.get_balance())

amount = int(input("Enter deposit amount: "))

account.deposit(amount)


print(account.get_balance())

amount = int(input("Enter amount: "))

account.withdraw(amount)

print(account.get_balance())