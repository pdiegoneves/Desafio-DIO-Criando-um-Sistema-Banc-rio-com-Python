from .client import Client


class Account:
    def __init__(self, account_number: int, client: Client):
        self.__balance = 0
        self.__withdrawal_limit = 3
        self.__max_withdrawal = 500
        self.__transactions = []
        self.__agency = "0001"
        self.__account_number = account_number
        self.__client = client

    @property
    def agency(self) -> str:
        return self.__agency

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def client(self) -> Client:
        return self.__client

    def deposit(self, value: float, /) -> bool:
        if value < 0:
            print("Não é possível depositar valores negativos.")
            return False
        self.__balance += value
        self.__transactions.append({"Depósito": value})
        print(f"Depósito de {value:.2f} realizado com sucesso!")
        return True

    def withdraw(self, /, value: float) -> bool:
        if value <= 0:
            print("O valor do saque deve ser positivo.")
            return False
        if self.__withdrawal_limit == 0:
            print("Você atingiu o limite de saques diários.")
            return False
        if value > self.__max_withdrawal:
            print(f"O valor máximo de saque é R$ {self.__max_withdrawal:.2f}")
            return False
        if value > self.__balance:
            print("Saldo insuficiente.")
            return False

        self.__balance -= value
        self.__transactions.append({"Saque": value})
        self.__withdrawal_limit -= 1
        print(f"Saque de {value:.2f} realizado com sucesso!")
        return True

    def show_transactions(self) -> None:
        print("=================================")
        print("Extrato:")
        print("=================================")
        for transaction in self.__transactions:
            for key, value in transaction.items():
                print(f"{key}: R$ {value:.2f}")

        print("=================================")
        print(f"Saldo: R$ {self.__balance:.2f}")
        print("=================================")

    def __str__(self):
        return (
            f"Agência: {self.agency}\n"
            f"C/C: {self.account_number}\n"
            f"Titular: {self.client.name}\n"
            f"CPF Titular: {self.client.cpf}"
        )
