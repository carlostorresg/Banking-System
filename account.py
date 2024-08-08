""" bank account """

class BankAccount:

    def __init__(self,name,):
        self.name = name 
        self.balance = 0.00
        self.transactions = []
        

    def deposit(self,amount):
        print(f"{self.name} {amount} was added to your bank account, your new balance is {self.balance + amount}")
        self.balance += amount 
        transaction = f"you deposit {amount} to your account"
        self.transactions.append(transaction)
        return self.balance
        
        
    def withdraw(self,amount):
        if amount > self.balance:
            return print("Insfucient fonds ")
        else:
            
            print(f"{self.name} {amount} was withdeaw from your bank account, your new balance is {self.balance - amount}")
            self.balance -= amount 
            transaction = f"you withdraw {amount} from you account"
            self.transactions.append(transaction)
            return self.balance
        
    
    def display_transactions(self):
        
        return "\n".join(self.transactions)
            

   
    def __str__(self):
        return (f"Your balance is {self.balance} ")

account = BankAccount("carlos")

account.deposit(400)
account.deposit(200)
account.withdraw(25)

print(account.display_transactions())

