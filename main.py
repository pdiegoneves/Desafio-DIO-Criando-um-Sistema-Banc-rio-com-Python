from src.acoount import Account

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """
    account = Account()
    while True:
        option = input(menu)
        
        match option:
            case 'd':
                value = float(input("Informe o valor do depósito: "))
                account.deposit(value)
            case 's':
                value = float(input("Informe o valor do saque: "))
                account.withdraw(value)
            case 'e':
                account.show_transactions()
            case 'q':
                break
            case _:
                print("Opção inválida, por favor selecione novamente a operação desejada.")

if __name__ == '__main__':
    main()