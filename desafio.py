from datetime import datetime


def menu_opcoes():
    menu = """
    =========== MENU ==========

    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta Corrente
    [6] Listar Usuários
    [7] Listar Contas
    [0] Sair

    ===========================

    => """
    
    return input(menu)


def depositar(valor, saldo, extrato, total_transacoes, /):
    if valor > 0:
        saldo += valor
        extrato += atualizar_extrato(valor=valor, tipo_transacao='Deposito')

        print("\nOperação realizada com sucesso!")
        
        return saldo, extrato, total_transacoes+1
    
    else:
        print('\nOperação falhou! O valor informado é inválido.')
    
    return saldo, extrato, total_transacoes


def sacar(*, valor, saldo, extrato, limite, total_saques, total_transacoes):
    if saldo < valor:
        print("\nOperação falhou! Saldo insuficiente.")

    elif valor > limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif valor > 0:
        saldo -= valor
        extrato += atualizar_extrato(valor=valor, tipo_transacao='Saque')
        
        print("\nOperação realizada com sucesso!")
        
        return saldo, extrato, total_saques+1, total_transacoes+1
    
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato,  total_saques, total_transacoes


def atualizar_extrato(*,valor, tipo_transacao):
    return (f"Tipo da Transação: {tipo_transacao}    Valor: R$ {valor:.2f}    Data da transação: {datetime.now()}\n")


def exibir_extrato(saldo, extrato):
    print(" EXTRATO ".center(100, "="))
    if not extrato: 
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("="*100)


def filtrar_usuarios(usuarios,cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def cadastrar_usuario(usuarios):
        nome_usuario = input('Nome completo do usuário: ')
        cpf = input('Informe o cpf(somente números): ')
        cpf = cpf.replace('.', '', 2)
        cpf = cpf.replace('-', '')
        
        existe_usuario = filtrar_usuarios(usuarios, cpf)
        
        if existe_usuario:
            print(f'\nJá existe usuário cadastrado com o CPF: {cpf}')
            return

        data_nascimento = input('Data de nascimento do usuário: ')
        logradouro = input('Digite o logradouro: ')
        numero = input('Digite o número do endereço: ')
        bairro = input('Digite o bairro: ')
        cidade = input('Digite a cidade: ')
        sigla_estado = input('Digite a sigla do estado: ')
        endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}'

        usuario = {
            'Nome': nome_usuario,
            'Data de Nascimento': data_nascimento,
            'CPF': cpf,
            'Endereço': endereco,
            }
        
        print ('\nUsuário cadastrado com sucesso!')

        usuarios.append(usuario)


def criar_conta_corrente(contas, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario_cadastrado = filtrar_usuarios(usuarios, cpf)

    if usuario_cadastrado:
        numero_conta = len(contas) + 1

        conta = {
            'Usuário': usuario_cadastrado['Nome'],
            'CPF': usuario_cadastrado['CPF'],
            'Número da Conta': numero_conta,
            'Agência': '0001'
        }

        contas.append(conta)
        print('\nConta criado com sucesso!')
    else:
        print('\nEsse usuário não está cadastrado!')


def listar_usuarios():
    pass


def listar_contas():
    pass
    


def main():
    saldo = 0
    limite = 500
    extrato = ''
    usuarios = []
    contas = []
    total_saques = 0
    total_transacoes = 0
    LIMITE_SAQUES = 3
    LIMITE_TRANSACOES = 10

    while True:
        opcao = menu_opcoes()

        if opcao == "1":
            if total_transacoes >= LIMITE_TRANSACOES:
                print ('Operação falhou! Número máximo de transações diárias excedido.')
                continue

            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato, total_transacoes = depositar(valor_deposito, saldo, extrato, total_transacoes)

        elif opcao == "2":
            if total_transacoes >= LIMITE_TRANSACOES:
                print ('Operação falhou! Número máximo de transações diárias excedido.')
                continue

            if total_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
                continue
            
            valor_saque = float(input("Digite o valor que deseja sacar: "))  
            saldo, extrato, total_saques, total_transacoes = sacar(valor=valor_saque, saldo=saldo, extrato=extrato, limite=limite, total_saques=total_saques, total_transacoes=total_transacoes)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == '4':
            cadastrar_usuario(usuarios)

        elif opcao == '5':
            criar_conta_corrente(contas, usuarios)

        elif opcao == '6':
            listar_usuarios(usuarios)
            pass
        
        elif opcao == '7':
            listar_contas(contas)
            pass

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novemente a operação desejada.")
    

main()