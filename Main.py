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
                if not id.isdigit():
                    print("INVALID ID")
                    continue
                
                elif len(id) > 8:
                    print("INVALID ID(MAX 8 DIGITS)")
                    continue
                break
            
            name = input("FULL NAME:")
            
            while True:

              email = input("EMAIL: ")
              if "@" not in email:
                print("INVALID EMAIL.")
                continue
              break    

            banco.create_client(id, name, email)
            

        elif option == "2":
            banco.create_account()

        elif option == "3":
            banco.search_account()
        
        elif option == "4":
            pass

        elif option == "5":
            print("THANKS FOR USING BANK'S")
            break

        else:
            print("INVALID OPTION.")

if __name__ == "__main__":
    principal()
