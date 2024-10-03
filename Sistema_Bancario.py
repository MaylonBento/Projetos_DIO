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
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro: valor inválido para depósito.")

    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))
        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("Operação falhou! Valor excede o limite.")
        elif numero_saque >= LIMITE_SAQUE:
            print("Operação falhou! Limite de saques atingido.")
        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Saque: R$ {valor:.2f}\n"
            numero_saque = numero_saque + 1
        else:
            print("Erro: valor inválido para saque.")

    elif opcao == "3":
        print("\n============== EXTRATO ==============")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")
