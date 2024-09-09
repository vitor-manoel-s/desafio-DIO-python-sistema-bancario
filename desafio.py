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
        print('Depositar')

    elif opcao == "1":
        if numero_saques_realizados < 3:

            print("Sacar")

    elif opcao == "2":
        print("Extrato")
    
    elif opcao == "3":
        break

    else:
        ("Operação inválida, por favor selecione novemente a operação desejada.")
    
