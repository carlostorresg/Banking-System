from .account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self,name,position):
        super().__init__(name,position)
        self.position = position 
        
