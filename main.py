from src.account import Account
from src.client import Client

USUARIOS = {}
CONTAS = {}


def get_main_menu_text():
    menu = """
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Lista contas
    [a] Acessar conta
    [q] Sair

    => """
    return menu


def get_submenu_input():
    menu = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [v]\tvoltar para o menu principal
    => """

    return input(menu)


def main():
    while True:
        option = input(get_main_menu_text())

        match option.lower():
            case "nu":
                name = input("Informe o nome do usuário: ")
                birthday = input("Informe a data de nascimento do usuário: ")
                cpf = input("Informe o CPF do usuário: ")
                address = input("Informe o endereço do usuário: ")
                user = Client(name, birthday, cpf, address)
                USUARIOS[cpf] = user
            case "nc":
                cpf = input("Informe o CPF do usuário: ")
                if cpf not in USUARIOS:
                    print("Usuário não encontrado.")
                    continue
                account_number = len(CONTAS) + 1
                account = Account(account_number, USUARIOS[cpf])
                CONTAS[account_number] = account
                print("Conta criada com sucesso!")
            case "lc":
                if not CONTAS:
                    print("Nenhuma conta cadastrada.")
                else:
                    print("\n=== LISTA DE CONTAS ===")
                    for acc in CONTAS.values():
                        print(str(acc))
                        print("--------------------")
            case "a":
                account_number_str = input("Informe o Número da conta: ")
                operations(account_number_str)
            case "q":
                print("Saindo do sistema...")
                break
            case _:
                print(
                    "Opção inválida, por favor selecione novamente a operação desejada."
                )


def operations(account_number_str: str):
    try:
        acc_num = int(account_number_str)
    except ValueError:
        print("Número da conta inválido. Deve ser um número.")
        return

    account = CONTAS.get(acc_num)
    if not account:
        print(f"Conta número {acc_num} não encontrada.")
        return

    while True:
        option = get_submenu_input()

        match option.lower():
            case "d":
                value = float(input("Informe o valor do depósito: "))
                account.deposit(value)
            case "s":
                value = float(input("Informe o valor do saque: "))
                account.withdraw(value=value)
            case "e":
                account.show_transactions()
            case "v":
                print("Voltando ao menu principal...")
                break
            case _:
                print(
                    "Opção inválida, por favor selecione novamente a operação desejada."
                )


if __name__ == "__main__":
    main()
