from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return f"Nome: {self.nome}    Cpf: {self.cpf}    Data de Nascimento: {self.data_nascimento}    Endereçe: {self.endereco}"


class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print('\nOperação falhou. Saldo insuficiente para realizar a operação!')
            return False

        elif valor > 0:
            self._saldo -= valor
            print('\nOperação realizada com sucesso')
            return True

        else:
            print('\nOperação falhou! O valor informado é inválido.')
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\nOperação realizada com sucesso!')
            return True
        
        else:
            print('\nOperação falhou! O valor informado é inválido.')
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, valor_limite_saque=500, limite_saques=3, limite_transacoes=10):
        super().__init__(numero, cliente)
        self._valor_limite_saque = valor_limite_saque
        self._limite_saques_diarios = limite_saques 
        self._limite_transacoes_diarias = limite_transacoes

    def sacar(self, valor):
        saldo = self._saldo
        saques_realizados = [transacao for transacao in self.historico.transacoes if transacao['Tipo']=='Saque']

        if len(self.historico.transacoes) >= self._limite_transacoes_diarias:
            print ('\nOperação falhou! Número máximo de trasações diários excedido.')
            return False
        
        elif len(saques_realizados) >= self._limite_saques_diarios:
            print ('\nOperação falhou! Número máximo de saques diários excedido.')
            return False
        
        elif valor > self._valor_limite_saque:
            print ('\nOperação falhou! O valor do saque excede o limite.')
            return False

        else:
            return super().sacar(valor)
        
        return False

    def depositar(self, valor):
        if len(self.historico.transacoes) >= self._limite_transacoes_diarias:
            print ('\nOperação falhou! Número máximo de trasações diários excedido.')
            return False
        
        else:
            return super().depositar(valor)
        
        return False

    def __str__(self):
        return f"Agência: {self.agencia}    Numero da Conta: {self.numero}  Titular: {self.cliente.nome}"

 
class Trasacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Trasacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        operacao_bem_sucedida = conta.depositar(self._valor)
        if operacao_bem_sucedida:
            conta.historico.adicionar_transacao(self)


class Saque(Trasacao):
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        operacao_bem_sucedida = conta.sacar(self._valor)
        if operacao_bem_sucedida:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'Tipo': transacao.__class__.__name__,
            'Valor': f'R${transacao._valor:.2f}',
            'Data': datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        })


def menu_opcoes():
    menu = """
=============================================== MENU ===============================================

[1] Cadastrar Cliente
[2] Criar Conta Corrente
[3] Depósito
[4] Saque
[5] Extrato da conta
[6] Listar Clientes
[7] Listar Contas
[0] Sair

=> """
    
    return input(menu)


def filtrar_clientes(clientes,cpf):
    usuarios_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def buscar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nEsse cliente não possui contas!")
        return
    
    for conta in cliente.contas:
        print(conta)

    nro_conta = int(input('\nInforme o número da conta: ')) # Solicita o número da conta em que será realizada a operação
    
    # Busca a conta em que será realizada a operação utilizando o número informado
    for conta in cliente.contas:
        if conta.numero == nro_conta:   
            conta_selecianada = conta
            return conta_selecianada    # retorna a conta em que será realizada a operação
    

def cadastrar_cliente(clientes):
    cpf = input('Informe o cpf(somente números): ')
    cpf = cpf.replace('.', '', 2)
    cpf = cpf.replace('-', '')
        
    cliente_cadastrado = filtrar_clientes(clientes, cpf)

    if cliente_cadastrado:
        print(f'\nJá existe um cliente cadastrado com o CPF: {cpf}')
        return

    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento(dd/mm/aa): ')
    logradouro = input('Digite o logradouro: ')
    numero = input('Digite o número do endereço: ')
    bairro = input('Digite o bairro: ')
    cidade = input('Digite a cidade: ')
    sigla_estado = input('Digite a sigla do estado: ')
    endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}'

    cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
    clientes.append(cliente)

    print ('\nUsuário cadastrado com sucesso!')


def criar_conta_corrente(clientes, contas):
    cpf = input('Informe o cpf(somente números): ')
    cpf = cpf.replace('.', '', 2)
    cpf = cpf.replace('-', '')
        
    cliente_cadastrado = filtrar_clientes(clientes, cpf)

    if cliente_cadastrado:
        conta = ContaCorrente.nova_conta(cliente_cadastrado, len(contas)+1)
        cliente_cadastrado.adicionar_conta(conta)
        contas.append(conta)
        print('\nConta criada com sucesso!')
    else:
        print('\nEsse usuário não está cadastrado!')


def depositar(clientes):
    cpf = input('Informe o cpf(somente números): ')
    cpf = cpf.replace('.', '', 2)
    cpf = cpf.replace('-', '')
        
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print('\nCliente não cadastrado!')
        return

    conta = buscar_conta_cliente(cliente)
    if not conta:
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Informe o cpf(somente números): ')
    cpf = cpf.replace('.', '', 2)
    cpf = cpf.replace('-', '')
        
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print('\nCliente não cadastrado!')
        return

    conta = buscar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input('Informe o cpf(somente números): ')
    cpf = cpf.replace('.', '', 2)
    cpf = cpf.replace('-', '')
        
    cliente = filtrar_clientes(clientes, cpf)

    if not cliente:
        print('\nCliente não cadastrado!')
        return

    conta = buscar_conta_cliente(cliente)
    if not conta:
        return
    
    print(" EXTRATO ".center(100, "="))
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas trasações."
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['Tipo']}: R$ {transacao['Valor']}        Data da Transação: {transacao['Data']}'

    print(extrato)
    print(f"\nSaldo:    R$ {conta.saldo:.2f}")


def listar_clientes(clientes):
    print(" CLIENTES ".center(100, "="))
    for cliente in clientes:
        print(cliente)


def listar_contas(contas):
    print(" CONTAS ".center(100, "="))
    for conta in contas:
        print(conta)


def main():
    clientes = []
    contas = []

    while True: 
        opcao = menu_opcoes()
        
        match opcao:

            case '1':
                cadastrar_cliente(clientes)
            case '2':
                criar_conta_corrente(clientes, contas)
            case '3':
                depositar(clientes)
            case '4':
                sacar(clientes)
            case '5':
                exibir_extrato(clientes)
            case '6':
                listar_clientes(clientes)
            case '7':
                listar_contas(contas)
            case '0':
                print('Saindo...')
                break
            case _:
                print("Operação inválida, por favor selecione novemente a operação desejada.")

main()