class BankAccount(object):

    balance = 0
    
    def __init__(self,name):
        self.name = name

    
    def __repr__(self):
        return("%s' account. Balance: $%.2f" % (self.name, self.balance))

    def show_balance(self):
        print("Balance: $%.2f" % self.balance)


    def deposit(self, amount):
        if amount <= 0:
            print("Number of money is invalid")
            return

        else:
            print("You deposited: %.2f" % amount)
            self.balance += amount
            self.show_balance()


    def withdraw(self, amount):
        if amount >= self.balance:
            print("Withdraw is invalid")
            return
        else:
            print("You withdraw: %.2f" % amount) 
            self.balance -= amount
            self.show_balance()


my_account = BankAccount("Duy")
print(my_account)
deposit_amount = float(input("Enter your deposit amount: "))
my_account.deposit(deposit_amount)
withdraw_amount = float(input("Enter your withdraw amount: "))
my_account.withdraw(withdraw_amount)
print(my_account)
