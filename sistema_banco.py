saldo_inicial = 0.00
saldo = 0.00

numero_saques = 0
LIMITE_SAQUES_DIARIO = 3
LIMITE_SAQUE = 500.00
saques = []

numero_depositos = 0
depositos = []

MENU = f"""
    Olá, sejam bem vindos ao nosso banco. Por favor, selecione a opção desejada:

    ================== Menu ==================
    
    1 - Sacar
    2 - Depositar
    3 - Ver extrato
    4 - Sair

Opção: """

EXTRATO_TITULO = f"""
    ================ Extrato ================

    Saldo inicial: R$ {saldo_inicial:.2f}
"""

def depositar():
    global numero_depositos, depositos, saldo
    
    while True:
        try:
            print()
            valor_depositado = float(input("Qual o valor o senhor(a) gostaria de depositar? "))
            if valor_depositado > 0.00:

                depositos.append(valor_depositado)
                numero_depositos += 1
                saldo += valor_depositado

                print()
                print(f"O valor R$ {valor_depositado:.2f} foi depositado")
                print(f"Seu saldo agora é de: R$ {saldo:.2f}")
                print()

                input("Pressione enter para continuar")
                break

            else:
                print()
                print("Valor inválido, por favor, tente novamente")
                print()
                input("Pressione enter para continuar")

        except ValueError:
            print()
            print("Por favor, digite um núemro válido")
            print()
            input("Pressione enter para continuar")

def sacar():
    global numero_saques, LIMITE_SAQUE, LIMITE_SAQUES_DIARIO, saques, saldo

    while True:
        print()
        print(f"Saldo disponível: {saldo:.2f}")
        print(f"Número de saques permitidos hoje: {LIMITE_SAQUES_DIARIO - numero_saques}")
        print()
        
        if numero_saques < LIMITE_SAQUES_DIARIO:
            try:
                valor_saque = float(input("Qual o valor o senhor gostaria de sacar? "))

                if (valor_saque > 0.00 and (valor_saque <= LIMITE_SAQUE) and (valor_saque <= saldo)):

                    saques.append(valor_saque)
                    numero_saques += 1
                    saldo -= valor_saque

                    print()
                    print(f"Valor de {valor_saque:.2f} foi sacado, por favor, retire seu dinheiro")
                    print(f"Seu saldo agora é de: RS {saldo:.2f}")
                    print()

                    input("Pressione enter para continuar")
                    break

                else:

                    if valor_saque > saldo:
                        print()
                        print(f"Saldo insulficiente, seu saldo é de {saldo:.2f}.")
                        print()
                        input("Pressione enter para continuar")
                        break

                    elif valor_saque > LIMITE_SAQUE:
                        print()
                        print(f"O limite de saque é de: {LIMITE_SAQUE}, por favor, escolha um valor abaixo desse limite")
                        print()
                        input("Pressione enter para continuar")
                        break
                            
                    elif valor_saque <= 0.00:
                        print()
                        print("Valor inválido, por favor, tente novamente")
                        print()
                        input("Pressione enter para continuar")
                        break

            except ValueError:
                print()
                print("Por favor, digite um núemro válido")
                print()
                input("Pressione enter para continuar")
        else:
            print()
            print(f"O limite de saques diários é de {LIMITE_SAQUES_DIARIO}, você já ultrapassou esse limite hoje")
            print()
            input("Pressione enter para continuar")
            break 

def ver_extrato():
    global saldo_inicial, saldo, numero_saques, saques, numero_depositos, depositos
    
    while True:
        print(EXTRATO_TITULO)

        if numero_depositos > 0:
            print("    =============== Depósitos ===============")
            print()
            print(f"    Número total de depósitos realizados: {numero_depositos}")
            print()

            i_deposito = 0
            for deposito in depositos:
                i_deposito += 1
                print(f"    Deposito {i_deposito}: R$ {deposito:.2f}")
            print()
        
        else:
            print("    Nenhum depósito realizado.")
            print()

        if numero_saques > 0:
            print("    ================ Saques =================")
            print()
            print(f"    Número total de saques realizados: {numero_saques}")
            print()

            i_saque = 0
            for saque in saques:
                i_saque += 1
                print(f"    Saque {i_saque}: RS {saque:.2f}")
            print()
        
        else:
            print("    Nenhum saque realizado")
            print()
        
        print("    =========================================")
        print()
        print(f"    Saldo atual: R$ {saldo:.2f}")
        print()
            
        input("Pressione enter para continuar")
        break

while True:
    menu_opcao = input(MENU)

    if menu_opcao == "1":
        sacar()
    elif menu_opcao == "2":
        depositar()
    elif menu_opcao == "3":
        ver_extrato()
    elif menu_opcao == "4":
        print("Obrigado por utilizar nossos serviços. Volte sempre!")
        break
    else:
        print("Opção não encontrada, por favor, tente novamente")
        