import getpass
import random
from opp2 import Client
from CuentaAhorro import SavingAccount
from CuentaCorriente import CurrentAccount

class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []
        self.load_data()
        
        
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
    
    def create_pin(self):
        while True:

            pin = getpass.getpass("CREATE 4-DIGIT PIN: ")

            if not pin.isdigit() or len(pin) != 4:
                print("INVALID PIN.")
                continue
            
            confirm = getpass.getpass("CONFIRM PIN: ")

            if pin != confirm:
                print("PIN DOES NOT MATCH")
                continue
            return pin
       
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

        print("ACCOUNT TYPE:")
        print("1 SAVING ACCOUNT")
        print("2 CURRENT ACCOUNT")

        account_type = input("ENTER: ")

        if account_type == "1":
            while True:
                try:
                  balance = float(input("INITIAL BALANCE:"))
                  break
                except:
                    print("INVALID AMOUNT")
            
            
            n_account = self.generate_account_number()
            
            cuenta = SavingAccount(n_account, balance, client_found)
            pin = self.create_pin()
            cuenta.pin = pin 

        elif account_type == "2":
            while True:
              entrada = input("INITIAL BALANCE(MIN $500) or x to cancel: ")
              
              if entrada.lower() == "x":
                  print("CANCELLED")
                  return
              
              try:
                  balance = float(entrada)

                  if balance < 500:
                      print("MINIMUN $500 REQUIRED.")
                      continue
                  break
              
              except:
                  print("INVALID AMOUNT")
                  return

            n_account = self.generate_account_number()

            overdraft = 500
           
            cuenta = CurrentAccount(n_account, balance, client_found, overdraft)
           
            pin = self.create_pin()
            cuenta.pin = pin

        else:
            print("INVALID OPTION.")
            return

        self.accounts.append(cuenta)
        client_found.accounts.append(cuenta)
        self.save_data()
        
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
            print("ACCOUNT NOT FOUND.")
            return
        
        pin_input = input("ENTER YOUR PIN: ")

        if pin_input != cuenta_origen.pin:
            print("INVALID PIN")
            return

        destino_num = input("ENTER DESTINATION ACCOUNT: ")
        cuenta_destino = None

        if num_origen == destino_num:
            print("CANNOT TRANSFER TO THE SAME ACCOUNT")
            return
        
        for account in self.accounts:
           if account.n_account == destino_num:
               cuenta_destino = account
               break
           
        if not cuenta_destino:
            print("DESTINATION NOT FOUND")
            return
        while True:
            try:
                amount = float(input("ENTER AMOUNT: "))

                if amount <= 0:
                    print("INVALID AMOUNT")
                    continue
                break

            except:
                print("INVALID INPUT")

        if not cuenta_origen.withdraw(amount):
            print("TRANSFER FAILED")
        
        else:
            cuenta_destino.deposit(amount)
            print("TRANSFER SUCCESSFUL")
    
    def save_data(self):
        import json

        data = []

        for client in self.clients:
            data.append({
                "id": client.id,
                "name": client.name,
                "email": client.email,
                "accounts": [
                    {
                        "n_account":acc.n_account,
                         "balance": acc.balance,
                         "type":acc.__class__.__name__,
                         "pin":getattr(acc, "pin", None)
                    }
                    for acc in client.accounts
                ]
                })
        with open("data.json", "w") as file:
            json.dump(data, file, indent = 4)

    def load_data(self):
        import json

        try:
            with open("data.json", "r") as file:
                data = json.load(file)

                for c in data:
                    client = Client(c["id"], c["name"], c["email"])

                    for acc in c["accounts"]:
                        if acc["type"] == "SavingAccount":
                            cuenta = SavingAccount(
                                acc["n_account"],
                                acc["balance"],
                                client
                            )
                        else:
                            cuenta = CurrentAccount(
                                acc["n_account"],
                                acc["balance"],
                                client,
                                500
                            )
                        cuenta.pin = acc["pin"]

                        client.accounts.append(cuenta)
                        self.accounts.append(cuenta)
                    
                    self.clients.append(client)
        except:
            pass
    