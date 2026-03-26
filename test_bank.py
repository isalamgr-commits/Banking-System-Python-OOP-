import unittest
from unittest.mock import patch

from Bank import Bank
from CuentaAhorro import SavingAccount
from opp2 import Client


class DummyAccount:
    def __init__(self, n_account):
        self.n_account = n_account


class BankTests(unittest.TestCase):
    def test_create_client_adds_new_client(self):
        bank = Bank()

        bank.create_client("1", "Alice", "alice@example.com")

        self.assertEqual(len(bank.clients), 1)
        client = bank.clients[0]
        self.assertIsInstance(client, Client)
        self.assertEqual(client.id, "1")
        self.assertEqual(client.name, "Alice")
        self.assertEqual(client.email, "alice@example.com")
        self.assertEqual(client.accounts, [])

    def test_generate_account_number_is_unique(self):
        bank = Bank()
        bank.accounts = [DummyAccount("111111111111")]

        with patch("random.randint", side_effect=[111111111111, 222222222222]):
            number = bank.generate_account_number()

        self.assertEqual(number, "222222222222")

    def test_find_client_returns_correct_client(self):
        bank = Bank()
        bank.create_client("1", "Alice", "alice@example.com")
        bank.create_client("2", "Bob", "bob@example.com")

        result = bank.find_client("2")

        self.assertIsNotNone(result)
        self.assertEqual(result.id, "2")
        self.assertEqual(result.name, "Bob")

    def test_create_account_creates_saving_account(self):
        bank = Bank()
        client = Client("1", "Alice", "alice@example.com")
        bank.clients.append(client)

        with patch("builtins.input", side_effect=["1", "1000", "1"]), patch.object(
            Bank, "generate_account_number", return_value="999999999999"
        ):
            bank.create_account()

        self.assertEqual(len(bank.accounts), 1)
        account = bank.accounts[0]
        self.assertIsInstance(account, SavingAccount)
        self.assertEqual(account.n_account, "999999999999")
        self.assertEqual(account.balance, 1000.0)
        self.assertIn(account, client.accounts)

    def test_transfer_moves_money_between_accounts(self):
        bank = Bank()
        client1 = Client("1", "Alice", "alice@example.com")
        client2 = Client("2", "Bob", "bob@example.com")
        account_origin = SavingAccount("111", 500.0, client1)
        account_dest = SavingAccount("222", 200.0, client2)
        bank.clients.extend([client1, client2])
        bank.accounts.extend([account_origin, account_dest])

        with patch("builtins.input", side_effect=["111", "222", "150"]):
            bank.transfer()

        self.assertEqual(account_origin.balance, 350.0)
        self.assertEqual(account_dest.balance, 350.0)


if __name__ == "__main__":
    unittest.main()
