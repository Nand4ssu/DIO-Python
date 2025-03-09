menu = """ 

[1] Depositar 
[2] Sacar
[3] Extrato
[4] Sair
>= """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    if opcao == 1:
        valor = float(input("Informe o valor do seu depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou! O valor é inválido.")
    elif opcao == 2:
        valor = float(input("Informe o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= limite_saques
        if excedeu_saldo:
            print("Operação não concluida! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação não concluída! Seu limite de saques foi atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor é inválido.")
    elif opcao == 3:
      print("\n ~~~~~~~~~~ EXTRATO ~~~~~~~~~~")
      print("Não teve movimentações realizadas." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif opcao == 4:
        break
    else:
        print("Opção inválida, por favor selecione a operação desejada")
        
    