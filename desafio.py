from datetime import date

menu = """


[0] Deposito
[1] Saque
[2] Extrato
[3] Sair


=> """


def sacar(*, valor, saldo, extrato, limite, total_saques, total_transacoes):
    if saldo < valor:
        print("Operação falhou! Saldo insuficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif valor > 0:
        saldo -= valor
        extrato += atualizar_extrato(valor=valor, tipo_transacao='Deposito')
        print("Operação realizada com sucesso!")
        return saldo, extrato, total_saques+1, total_transacoes+1
    else:
        print("Operação falhou! O valor informado é inválido.")


def atualizar_extrato(*,valor, tipo_transacao):
    return (f"Tipo da Transação: {tipo_transacao}    Valor: R$ {valor:.2f}    Dia da transação: {date.today()}\n")


def exibir_extrato(saldo, extrato):
    print(" EXTRATO ".center(100, "="))
    if not extrato: 
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("="*100)


def main():
    saldo = 0
    limite = 500
    extrato = ''
    total_saques = 0
    total_transacoes = 0
    LIMITE_SAQUES = 3
    LIMITE_TRANSACOES = 10

    while True:
        opcao = input(menu)

        if opcao == "0":
            if total_transacoes >= LIMITE_TRANSACOES:
                print ('Operação falhou! Número máximo de transações diárias excedido.')
                continue

            valor_deposito = float(input("Digite o valor que deseja depositar: "))

            if valor_deposito > 0:
                saldo += valor_deposito
                total_transacoes += 1
                extrato += (f"Tipo da Transação: Deposito    Valor: R$ {valor_deposito:.2f}    Dia da transação: {date.today()}\n")
                print('Operação realizada com sucesso!')
            else:
                print('Operação falhou! O valor informado é inválido.')

        elif opcao == "1":
            if total_transacoes >= LIMITE_TRANSACOES:
                print ('Operação falhou! Número máximo de transações diárias excedido.')
                continue

            if total_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
                continue
            
            valor_saque = float(input("Digite o valor que deseja sacar: "))  
            saldo, extrato, total_saques, total_transacoes = sacar(valor=valor_saque, saldo=saldo, extrato=extrato, limite=limite, total_saques=total_saques, total_transacoes=total_transacoes)

        elif opcao == "2":
            exibir_extrato(saldo, extrato)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            ("Operação inválida, por favor selecione novemente a operação desejada.")
    

main()