import requests


class Database:
    @classmethod
    def clear_database(cls):
        requests.post("https://parabank.parasoft.com/parabank/services/bank/cleanDB")

    @classmethod
    def start_database(cls):
        requests.post("https://parabank.parasoft.com/parabank/services/bank/initializeDB")
