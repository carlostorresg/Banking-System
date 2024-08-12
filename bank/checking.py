from .account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self,name,overdraft_limit=100):
        super().__init__(name)
        self.overdraft_limit = overdraft_limit
        
        
    def withdraw(self,amount):
        '''
        Withdrawing with an overdraft limit of 100 
        '''
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            transaction = f'You withdraw {amount} from your checking account'
            self.transactions.append(transaction)
            
        else:
            print("Insufficient fonds ")
        
        return self.balance

    







        
