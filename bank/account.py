

class BankAccount:

    def __init__(self,name):
        self.name = name 
        self.balance = 0.00
        self.transactions = []
        

    def deposit(self,amount):
       
        
        self.balance += amount 
        transaction = f"you deposit {amount} to your account"
        self.transactions.append(transaction)
        return self.balance
        
        
    def withdraw(self,amount):
        if amount > self.balance:
             print("Insffucient fonds ")
             return self.balance
        else:
            
            
            self.balance -= amount 
            transaction = f"you withdraw {amount} from you account"
            self.transactions.append(transaction)
            return self.balance
        
    
    def display_transactions(self):
        '''List with all your transactions made'''
        
        return "\n".join(self.transactions)
            

   
    def __str__(self):
        return (f"Your balance is {self.balance} ")




