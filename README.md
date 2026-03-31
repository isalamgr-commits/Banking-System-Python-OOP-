Banking System (PYTHON OOP)

Description

This is a console-based banking system developed using Object-Oriented Programming (OOP).

It simulates basic banking operations such as client management, account creation, and money transfers.

Features

- Crear nuevos clientes
- Generar números de cuenta únicos de 12 dígitos
- Sistema de PIN seguro de 4 dígitos (entrada oculta)
- Depositar y retirar dinero
- Transferencias internas (mismo banco)
- Transferencias externas (con comisión)
- Persistencia de datos con JSON (los datos se guardan incluso después de cerrar el programa)
- Validaciones de entrada (correo electrónico, ID, saldo, etc.)

Technologies Used

.Python 3
.Object-Oriented Programming (OOP)
.JSON
.getpass


ESTRUCTURA DEL PROYECTO

/PROYECTO
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
