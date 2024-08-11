from .account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self,name):
        super().__init__(name)
        
        

    
    def withdraw_overdraft(self,amount,overdraft=100):

        
        if self.balance + overdraft > amount:
            self.balance -= amount
            print(f"You withdraw {amount} from your card ")
            transaction = f'You withdraw {amount} from your card'
            self.transactions.append(transaction)
            return self.balance



carlos = CheckingAccount("carlos")
carlos.withdraw_overdraft(20)
        



        
