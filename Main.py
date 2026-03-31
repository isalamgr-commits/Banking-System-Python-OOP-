from Bank import Bank
from opp2 import Client

def principal():
    banco = Bank()
    

    while True:
        print("\n--- MENU ---")
        print("1 NEW CLIENT")
        print("2 CREATE ACCOUNT")
        print("3 SEARCH ACCOUNT")
        print("4 TRANFER")
        print("5 EXIT")

        option = input(("SELECT OPTION: "))
      
        if option == "1":
            
            while True:
                id = input("ID: ")

                if id.strip() == "":
                    print("ENTER YOUR ID.")
                    continue

                if not id.isdigit():
                    print("INVALID ID")
                    continue
                
                elif len(id) > 8:
                    print("INVALID ID(MAX 8 DIGITS)")
                    continue
                break
            
            while True:
                name = input("FULL NAME:")
                if name == " ":
                    print("PLEASE, ENTER A NAME.")
                    continue
                if not name.replace(" ","").isalpha():
                    print("PLEASE, ENTER A VALID NAME")
                    continue
                break
            
            while True:

              email = input("EMAIL: ").strip()
              if "@" not in email:
                print("INVALID EMAIL.")
                continue
              if email == "":
                  print("INVALID EMAIL.")
                  continue
              
              if " " in email:
                  print("INVALID EMAIL.")
                  continue
              
              valid_domains = ["@gmail.com",
                               "@outlook.com",
                               "@hotmail.com",
                               "@edu.pe",
                               "@uni.edu"]

              if not any(email.endswith(domain) for domain in valid_domains):
                  print("INVALID EMAIL")
                  continue
              break    

            banco.create_client(id, name, email)     

        elif option == "2":
            banco.create_account()

        elif option == "3":
            banco.search_account()
        
        elif option == "4":
            print("TRANFER TYPE:")
            print("1 INTERNAL")
            print("2 EXTERNAL")

            transfer_option = input("SELECT:")

            if transfer_option == "1":
                banco.transfer()

            elif transfer_option == "2":
                origen = input("ENTER YOUR ACCOUNT: ")
                cuenta_origen = None

                for acc in banco.accounts:
                    if acc.n_account == origen:
                        cuenta_origen = acc
                        break
                
                if not cuenta_origen:
                    print("ACCOUNT NOT FOUND")
                    continue
                
                external_account = input("ENTER DESTINATION ACCOUNT:")
                
                if origen == external_account:
                    print("CANNOT TRANSFER TO SAME ACCOUNT")
                    continue

                bank_name = input("ENTER BANK NAME: ")

                attempts = 3
                
                while attempts > 0:
                    pin_input = input("ENTER YOUR PIN: ")       
                
                    if pin_input == cuenta_origen.pin:
                        break

                    attempts -= 1
                    print(F"INVALID PIN. ATTEMPTS LEFT: {attempts}")

                    if attempts == 0:
                      print("ACCOUNT BLOCKED")
                      return
                
                while True:
                    try:
                        amount = float(input("ENTER AMOUNT: "))
                        if amount <= 0:
                            print("INVALID AMOUNT")
                            continue
                        break
                    except:
                        print("INVALID INPUT.")
                
                fee = 5
                total = amount + fee

                print("\n---EXTERNAL TRANFER---")
                print(f"FROM: {cuenta_origen.n_account}")
                print(f"TO: {external_account}")
                print(f"BANK: {bank_name}")
                print(f"AMOUNT: {amount}")
                print(f"FEE: {fee}")

                confirm = input(f"CONFIRM TRANFER ${total} ? (y/n): ")

                if confirm.lower() != "y":
                    print("CANCELLED")
                    continue

                if not cuenta_origen.withdraw(total):
                        print("TRANSFER FAILED (INSUFICIENT FUNDS)")
                        continue

                print("----TRASNFER SUCCESFULL----")
                print(f"FROM: {cuenta_origen.n_account}")
                print(f"TO: {external_account}")
                print(f"BANK: {bank_name}")
                print(f"AMOUNT: {amount}")
                print(f"FEE: {fee}")
                print(f"TOTAL: ${total}")
                print("STATUS: SENT")

        elif option == "5":
            print("THANKS FOR USING BANK'S")
            break

        else:
            print("INVALID OPTION.")

if __name__ == "__main__":
    principal()
