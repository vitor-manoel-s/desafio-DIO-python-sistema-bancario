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
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


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

        elif valor > 0:
            return super().sacar(valor)
        
        return False

    def depositar(self, valor):
        if len(self.historico.transacoes) >= self._limite_transacoes_diarias:
            print ('\nOperação falhou! Número máximo de trasações diários excedido.')
            return False
        
        elif valor > 0:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"Agência: {self.agencia}\nNumero da Conta: {self.numero}\nTitular: {self.cliente._nome}"

 
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