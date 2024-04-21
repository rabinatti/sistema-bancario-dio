menu = """
    Olá, sejam bem vindos ao nosso banco. Por favor, selecione a opção desejada:

    ================== Menu ==================
    
    1 - Ver extrato
    2 - Depositar
    3 - Sacar
    4 - Sair

Opção: """

saldo_inicial = 0.00
saldo = 0.00

numero_saques = 0
LIMITE_SAQUES_DIARIO = 3
LIMITE_SAQUE = 500.00
saque = []

numero_depositos = 0
deposito = []

def depositar():
    global numero_depositos, saldo
    
    while True:
        try:
            valor_depositado = float(input("Qual o valor o senhor(a) gostaria de depositar? "))
            if valor_depositado > 0.00:

                print(" ")
                print(f"O valor R$ {valor_depositado:.2f} foi depositado")

                deposito.append(valor_depositado)
                numero_depositos += 1
                saldo += valor_depositado

                print(f"Seu saldo agora é de: R$ {saldo:.2f}")

                input("Pressione enter para continuar")
                break

            else:
                print("Valor inválido, por favor, tente novamente")

        except ValueError:
            print("Por favor, digite um núemro válido")

def sacar():
    global numero_saques, LIMITE_SAQUE, LIMITE_SAQUES_DIARIO, saque, saldo

    while True:
        if numero_saques < LIMITE_SAQUES_DIARIO:
            try:
                valor_saque = float(input("Qual o valor o senhor gostaria de sacar? "))

                if (valor_saque > 0.00 and (valor_saque <= LIMITE_SAQUE) and (valor_saque <= saldo)):

                    saque.append(valor_saque)
                    numero_saques += 1
                    saldo -= valor_saque

                    print(f"Valor de {valor_saque:.2f} foi sacado, por favor, retire seu dinheiro")
                    print(f"Seu saldo agora é de: RS {saldo:.2f}")

                    input("Pressione enter para continuar")
                    break

                else:

                    if valor_saque > saldo:
                        print(" ")
                        print(f"Saldo insulficiente, seu saldo é de {saldo:.2f}.")
                        input("Pressione enter para continuar")
                        break

                    elif valor_saque > LIMITE_SAQUE:
                        print(" ")
                        print(f"O limite de saque é de: {LIMITE_SAQUE}, por favor, escolha um valor abaixo desse limite")
                        input("Pressione enter para continuar")
                        break
                            
                    elif valor_saque <= 0.00:
                        print(" ")
                        print("Valor inválido, por favor, tente novamente")
                        input("Pressione enter para continuar")
                        break

            except ValueError:
                print("Por favor, digite um núemro válido")
        else:
            print(f"O limite de saques diários é de {LIMITE_SAQUES_DIARIO}, você já ultrapassou esse limite hoje")
            break 

while True:
    menu_opcao = input(menu)

    if menu_opcao == "1":
        print("Extrato")
        break
    elif menu_opcao == "2":
        depositar()
    elif menu_opcao == "3":
        sacar()
    elif menu_opcao == "4":
        print("Obrigado por utilizar nossos serviços. Volte sempre!")
        break
    else:
        print("Opção não encontrada, por favor, tente novamente")
        