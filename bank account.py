class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    
    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

account1 = BankAccount("Semira Kemal", 400)


account1.deposit(50)
account1.withdraw(30)
account1.display()


    