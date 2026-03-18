from Cuenta import Account

class CurrentAccount(Account):
    def __init__(self,n_account,balance, client, overdraft_limit):
        super().__init__(n_account,balance, client)
        self.overdraft_limit = overdraft_limit
    
    def overdraft_interest(self,amount,rate = 0.139 ,days= 1):
       if amount <= 0:
           return 0
       
       daily_rate =  rate / 365
       interest = amount * daily_rate * days

       return interest

    def withdraw(self, amount):
        if  amount <= 0:
            print("INVALID AMOUNT.")
            return False
        
        if amount > self.balance + self.overdraft_limit:
            print("OVERDRAFT LIMIT EXCEEDED.")
            return False
        
        self.balance -= amount
        return True