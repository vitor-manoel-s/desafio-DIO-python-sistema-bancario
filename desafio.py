menu = """


[0] Deposito
[1] Saque
[2] Extrato
[3] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques_realizados = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato = extrato + f"Deposito: R$ {valor_deposito:.2f}\n"
            print('Operação realizada com sucesso!')
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "1":
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        
        if saldo < valor_saque:
            print("Operação falhou! Saldo insuficiente.")

        elif numero_saques_realizados >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques_realizados += 1
            extrato = extrato + f"Saque: R$ {valor_saque:.2f}\n"
            print("Operação realizada com sucesso!") 

        else:
            print("Operação falhou! O valor informado é inválido.")     

    elif opcao == "2":
        print(" EXTRATO ".center(50, "="))
        if not extrato: 
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("="*50)

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        ("Operação inválida, por favor selecione novemente a operação desejada.")
    
