from bank.account import BankAccount
from bank.checking import CheckingAccount
from bank.savings import SavingsAccount



if __name__ == '__main__':

    bank = BankAccount("Carlos")
    checkings = CheckingAccount("Carlos")
    savings = SavingsAccount("Carlos")

    
# Starting with regular Bank Account
    
    print(bank)
    bank.deposit(500)
    bank.withdraw(50)
    print(bank.display_transactions())
    print(bank)
    print("----------------------------------------")
    

# Checkings Account , in the checkings account you have overdraft limit of 100

    print(checkings)
    checkings.deposit(500)
    '''
    Overdrafting the account to the limt of 100
    '''
    checkings.withdraw(600)
    print(checkings.display_transactions())
    
    ''' 
    If you want to withdraw more than the overdraft limit 
    ,it is going to result on Insufficient fonds '''
    checkings.withdraw(1)
    print(checkings)
    print("----------------------------------------")

# Savings Account , you get interest every time you deposit 
    print(savings)
    savings.deposit(100)
    savings.apply_interest()
    print(savings.display_transactions())
    print(savings)




    



    

    

    
   


    




