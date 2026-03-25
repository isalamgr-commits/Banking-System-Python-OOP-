import random
from opp2 import Client
from CuentaAhorro import SavingAccount
from CuentaCorriente import CurrentAccount

class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []
        
    def create_client(self, id, name, email):
        cliente = Client(id, name, email) # type: ignore
        self.clients.append(cliente)
    
    def generate_account_number(self):
            while True:
                number = str(random.randint(100000000000,999999999999))

                exists = False
                
                for account in self.accounts: # type: ignore
                    if account.n_account == number:
                        exists = True
                        break

                if not exists:
                    return number

    def find_client(self, id):
      for client in self.clients:
         if client.id == id:
             return client
      return None
           
    def create_account(self):
        client_id = input("ENTER THE CLIENT ID: ")
        client_found= None
        
        for client in self.clients:
           if client.id == client_id:
                client_found = client
                break
           
        if not client_found:
            print("CLIENT NOT FOUND.")
            return
        
        n_account = self.generate_account_number()
        balance = float(input("INITIAL BALANCE:"))
        
        print("ACCOUNT TYPE:")
        print("1 SAVING ACCOUNT")
        print("2 CURRENT ACCOUNT")

        account_type = input("ENTER: ")

        if account_type == "1":
            cuenta = SavingAccount(n_account, balance, client_found)

        elif account_type == "2":
            overdraft = 1000
            cuenta = CurrentAccount(n_account, balance, client_found, overdraft)

        else:
            print("INVALID OPTION.")
            return

        self.accounts.append(cuenta)
        client_found.accounts.append(cuenta)
        
        print("ACCOUNT CREATED SUCCESSFULLY.")
        print(f"ACCOUNT NUMBER: {n_account}")
    
    def search_account(self):
        n_account = input("ENTER ACCOUNT NUMBER: ")
        for account in self.accounts:
            if account.n_account == n_account:
                print("ACCOUNT FOUND.")
                account.show_info()
                return account
        
        print("ACCOUNT NOT FOUND.")
        return None

    def transfer(self):
        num_origen = input("ENTER ACCOUNT NUMBER: ")
        cuenta_origen = None
        
        for account in self.accounts:
            if account.n_account == num_origen:
                cuenta_origen = account
                break
        
        if not cuenta_origen:
            print("ACCOUNR NOT FOUND.")
            return
        
        destino_num = input("ENTER DESTINATION ACCOUNT: ")
        cuenta_destino = None
        
        for account in self.accounts:
           if account.n_account == destino_num:
               cuenta_destino = account
               break
           
        if not cuenta_destino:
            print("DESTINATION NOT FOUND")
            return
        
        amount = float(input("ENTER AMOUNT: "))

        if not cuenta_origen.withdraw(amount):
            print("TRANSFER FAILED")
        
        else:
            cuenta_destino.deposit(amount)
            print("TRANSFER SUCCESSFUL")

        