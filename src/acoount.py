class Account:
    def __init__(self):
        self.__balance = 0
        self.__withdrawal_limit = 3
        self.__max_withdrawal = 500
        self.__transactions = []
        
    def deposit(self, value: float) -> bool:
        if value < 0:
            print("Não é possível depositar valores negativos.")
            return False
        self.__balance += value
        self.__transactions.append({"Depósito": value})
        print(f"Depósito de {value:.2f} realizado com sucesso!")
        return True
    
    def withdraw(self, value: float) -> bool:
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