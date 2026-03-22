from CuentaAhorro import SavingAccount
from CuentaCorriente import CurrentAccount

class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []
        
    def create_client(self, name, email, id):
        cliente = Cliente(name, email, id) # type: ignore
        self.clients.append(cliente)

    def create_account(self):
        client_id = input("ENTER THE CLIENT ID: ")
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
            cuenta = SavingAccount()
        elif account_type == "2":
            cuenta = CurrentAccount()

        client.accounts.append(cuenta)
        client_found.cuentas.append(cuenta)

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
        cuenta_origen = input("ENTER ACCOUNT NUMBER: ")
        for account in self.accounts:
            if account.cuenta_origen == cuenta_origen:
                account.show_info()
                print("ENTER ACCOUNT TO TRANFER: ")
            else:
                print("ACCOUNT NOT FOUND.")