import re


class Client:
    def __init__(self, name, birthday, cpf, address):
        self.__name = name
        self.__birthday = birthday
        self.__cpf = cpf
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday

    @property
    def cpf(self):
        return self.__cpf

    @property
    def address(self):
        return self.__address

    @cpf.setter
    def cpf(self, new_cpf):
        if not new_cpf.isnumeric():
            print("CPF inválido")
            return

        new_cpf = re.compile(r"[^0-9]").sub("", new_cpf)

        if len(new_cpf) != 11:
            print("CPF inválido")
            return

        self.__cpf = new_cpf

    @address.setter
    def address(self, new_address):
        if "," not in new_address or "-" not in new_address or "/" not in new_address:
            print("Endereço inválido")
            return
        self.__address = new_address

    def __str__(self):
        return f"Nome: {self.name}, CPF: {self.cpf}"
