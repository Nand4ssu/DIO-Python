import textwrap #biblioteca utilizada para manipular textos (ela ajusta a identação do menu)


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [nvc]\tNova conta
    [lc]\tListar contas
    [nvu]\tNovo usuário
    [e]\tSair
    => """
    # O \t insere um espaço de tabulação (tecla tab) horizontal no texto. 
    return input(textwrap.dedent(menu)) #Remove a indentação e exibe o menu formatado


def depositar(saldo, valor, extrato, /): #A Barra obriga os primeiros argumentos a serem apenas posicionais
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falha! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # O # Asterisco obriga os parâmetros a serem passados nomeados
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falha! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falha! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falha! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falha! O valor informado é inválido. Por favor digite um valor válido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ Extrato ================")
    # Caso não houver movimentações, informa o que está escrito abaixo.
    print("Não foram realizadas movimentações." if not extrato else extrato)
    #Exibe o saldo atual.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    # O f-string é uma maneira de inserir variáveis dentro de uma String de forma fácil e legível.
    #:.2f formata o número para ter duas casas decimais, no estilo de valor monetário (exemplo: 100.00).
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Digite o seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um cadastro com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    # Adiciona um novo usuário à lista de usuários.
    # Cada usuário é representado como um dicionário contendo, nome, data de nascimento, CPF e endereço.
    # A função append() insere esse dicionário no final da lista 'usuarios'.
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nvu":
            criar_usuario(usuarios)

        elif opcao == "nvc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "e":
            break # O break encerra o loop e sai do programa.

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
