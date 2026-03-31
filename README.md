Banking System (PYTHON OOP)

Description

This is a console-based banking system developed using Object-Oriented Programming (OOP).

It simulates basic banking operations such as client management, account creation, and money transfers.

Features

-Create new clients
-Generate unique 12-digit account numbers
-Secure 4-digit PIN system (hidden input)
-Deposit and withdraw money
-Internal transfers (same bank)
-External transfers (with fee)
-Data persistence using JSON (data is saved even after closing the program)
-Input validations (email, ID, balance, etc.)

Technologies Used

.Python 3
.Object-Oriented Programming (OOP)
.JSON
.getpass


PROJECT STRUCTURE

/PROJECT

│── Main.py
│── Bank.py
│── Cuenta.py
│── CuentaAhorro.py
│── CuentaCorriente.py
│── opp2.py (Cliente)
│── data.json

How to Run

Open terminal in the project folder
Run:

python Main.py

SECURITY
Each account is protected with a 4-digit PIN.

The PIN is required for transfers.
The login information is hidden using getpass.

Important Note

-This is a simulation project (without real bank integration, for practice purposes only).

-PINs are stored in plain text (for educational purposes).
