from .account import BankAccount


class SavingsAccount(BankAccount):

    '''
    Making savings class inheriting the BankAccount class'''

    def __init__(self,name,interest=0.05):
     super().__init__(name)
     self.interest = interest
     

    def apply_interest(self):
       '''
       Deposits the interest 
       '''
       interest = self.balance * self.interest
       self.deposit(interest)
       return interest

