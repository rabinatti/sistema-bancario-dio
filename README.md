# Bootcamp da [DIO](https://web.dio.me/)

Projeto realizado como desafio no Bootcamp da [DIO](https://web.dio.me/), [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer). 

**Desafio:** Criando um Sistema Bancário com Python

## Linguagem utilizada:
* Python

## Descrição e regras do desafio:
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

### Operações de Depósito:
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operações de saque:
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operações de extrato:
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: **Não foram realizadas movimentações**

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

1500.45 = R$ 1500.45

## Mudanças realizadas
Para esse projeto, realizei algumas mudanças, como:

 - A criação e a chamada de métodos, ao invés de escrever o codigo todo no menu incial como era aoresentado no template. Para isso fiz pesquisas de como criar e chamar métodos utilizando o Python.

 - Na hora que o usuário digitasse um valor para sacar ou depositar, ele deveria digitar um valor do tipo **float**, se o usuário digitasse alguma letra ou **string**, o programa retornava um erro e travava. Para impedir isso fiz uma pesquisa e utilizei o método **try/except** para que caso o usúario digitasse um valor inválido, o programa iria exibir uma mensagem de erro, e iria reiniciar a operação para que o usuário pudesse então digitar um valor válido.
