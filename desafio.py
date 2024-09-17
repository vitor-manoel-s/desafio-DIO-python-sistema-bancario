from datetime import date

menu = """


[0] Deposito
[1] Saque
[2] Extrato
[3] Sair


=> """

saldo = 0
limite = 500
extrato = ''
numero_saques_realizados = 0
numero_transacoes_realizadas = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10

while True:
    opcao = input(menu)

    if opcao == "0":
        if numero_transacoes_realizadas >= LIMITE_TRANSACOES:
            print ('Operação falhou! Número máximo de transações diárias excedido.')
            continue

        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            numero_transacoes_realizadas += 1
            extrato += (f"Tipo da Transação: Deposito    Valor: R$ {valor_deposito:.2f}    Dia da transação: {date.today()}\n")
            print('Operação realizada com sucesso!')
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "1":
        if numero_transacoes_realizadas >= LIMITE_TRANSACOES:
            print ('Operação falhou! Número máximo de transações diárias excedido.')
            continue

        if numero_saques_realizados >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            continue
        
        valor_saque = float(input("Digite o valor que deseja sacar: "))
            
        if saldo < valor_saque:
            print("Operação falhou! Saldo insuficiente.")

        elif valor_saque > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques_realizados += 1
            numero_transacoes_realizadas += 1
            extrato += (f"Tipo da Transação: Saque    Valor: R$ {valor_saque:.2f}    Dia da transação: {date.today()}\n")
            print("Operação realizada com sucesso!") 

        else:
            print("Operação falhou! O valor informado é inválido.")     

    elif opcao == "2":
        print(" EXTRATO ".center(100, "="))
        if not extrato: 
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("="*100)

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        ("Operação inválida, por favor selecione novemente a operação desejada.")
    
