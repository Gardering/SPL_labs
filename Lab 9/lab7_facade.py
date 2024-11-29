from labs.lab7.api.api_client import APIClient
from labs.lab7.api.repository import DataRepository
from labs.lab7.core.transaction import Transactions
from labs.lab7.ui.user_interface import UserInterface
from labs.lab7.core.error_handler import ErrorHandler

class Lab7Facade:
    def __init__(self):
        self.api_client = APIClient("https://jsonplaceholder.typicode.com")
        self.repository = DataRepository(self.api_client)
        self.transactions = Transactions()
        self.ui = UserInterface(self.repository, self.transactions)

    def execute(self):
        """
        Запуск лабораторної роботи 7.
        """
        print("\n=== Лабораторна 7: Робота з API ===")
        try:
            self.ui.start()
            self.transactions.save_history()
        except Exception as e:
            ErrorHandler.handle_error(e)