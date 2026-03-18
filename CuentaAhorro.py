from Cuenta import Account

class SavingAccount(Account):
    def __init__(self,n_account,balance, client):
        super().__init__(n_account,balance, client)
    
    def calculate_interest(self, rate = 0.05):
        return self.balance * rate
    
    def apply_interest(self): 
        interest = self.calculate_interest()
        self.balance += interest

