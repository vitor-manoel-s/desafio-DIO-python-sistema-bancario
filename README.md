﻿## Desafio 1: Criando um sistema bancário

### Objetivo
Criar um sistema bancário com as operações: sacar, depositar
e visualizar extrato.

- Operação de depósito: Deve ser possível depositar valores positivos para a minha
conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
dessa forma não precisamos nos preocupar em identificar qual
é o número da agência e conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na
operação de extrato.

- Operação de saque: O sistema deve permitir realizar 3 saques diários com limite
máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem
informando que não será possível sacar o dinheiro por falta de
saldo. Todos os saques devem ser armazenados em uma
variável e exibidos na operação de extrato.

- Operação de extrato: Essa operação deve listar todos os depósitos e saques
realizados na conta. No fim da listagem deve ser exibido o
saldo atual da conta. Se o extrato estiver em branco, exibir a
mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
exemplo:
1500.45 = R$ 1500.45


## Desafio 2: Otimizando o Sistema Bancário com Funções Python

### Objetivo
- Aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas

- Criar duas novas funções para criar usuário e criar conta corrente.

## Desafio 3: Modelando o Sistema Bancário em POO com Python

### Objetivo
- Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.
