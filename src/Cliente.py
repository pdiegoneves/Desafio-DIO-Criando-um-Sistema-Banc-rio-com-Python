class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adcionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        for i, conta in enumerate(self._contas):
            print(f"Conta {i + 1}: {conta}")


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if len != 10:
            raise ValueError("CPF inválido")

        self._cpf = cpf
