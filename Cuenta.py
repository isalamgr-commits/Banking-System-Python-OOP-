class Account:
    def __init__(self,n_account,balance,client):
        self.n_account=n_account
        self.balance=balance
        self.client=client

    def deposit(self,amount):
        
        if amount <= 0:
            print("INVALID AMOUNT.") 
            return False
        
        self.balance=self.balance+amount
        return True

    def withdraw(self,amount):

        if amount <= 0:
            print("PLEASE, ENTER A VALID AMOUNT.")
            return False

        if amount > self.balance:
            print("INSUFFICIENT FUNDS.")
            return False

        self.balance=self.balance-amount
        return True
    
    def show_info(self):
        print(f"ACCOUNT: {self.n_account}")
        print(f"CLIENT: {self.client}")
        print(f"BALANCE: $ {self.balance:.2f}")

cuenta = Account("461798712",239, "MARCO PEÑA SOLIS")
cuenta.show_info()