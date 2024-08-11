from .account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self,name):
        super().__init__(name)
        
        

    
    def withdraw_od(self,amount,overdraft=100):
        '''
        Withdrawing with an overdraft limit of 100 
        '''
        withdraw = amount
        
        if self.balance + overdraft >= withdraw:
            self.balance -= withdraw
            print(f"You withdraw {withdraw} from your card ")
            transaction = f'You withdraw {withdraw} from your card'
            self.transactions.append(transaction)
            return withdraw
        
        else:
            print("Insuficient fonds ")







        
