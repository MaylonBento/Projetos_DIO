menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro ao realizar a operação, valor inválido")

    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficente.")

        elif excedeu_limite:
            print("Operação falhou! Valor solicitado excede limite permitido.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de sques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque  += 1

        else:
            print("Erro ao realizar saque, valor inválido")
            

    elif opcao == "3":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movientações." if not extrato else extrato)
        print(f"\n Saldo R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "0":
        break

    else:
        print("Opção invalida, selecione uma opção valida")

