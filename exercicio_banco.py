<<<<<<< HEAD
def menu():
    menu = """ 
    Escolha uma opção: 

    [1] Depositar 
    [2] Sacar 
    [3] Extrato 
    [4] Novo usuário 
    [5] Nova conta
    [6] Mostrar contas
    [0] Sair
    A opção escolhida foi:  """ 
    return input(menu)
    
def cadastrar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dia/mês/ano. Ex: 01/01/2000): ")
    endereco = input ("Informe seu endereço (logradouro, número, bairro, cidade (sigla), estado (sigla)): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereço": endereco})

    print("Usuário criado com sucesso!")
     
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta_bancaria(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario nao encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= limite_saques 

    if excedeu_saldo:
        print("Você não tem saldo suficiente para reliazar essa operação.")

    elif excedeu_limite:
        print("Valor limite do saque excedido! O valor máximo para cada saque é de até R$500,00")
            
    elif excedeu_saques:
        print("O limite é de até 3 saques por dia.")
            
    elif valor > 0:
            saldo -= valor
            extrato += f"saque R$ {valor:.2f}"
            numero_de_saques += 1
            print("Saque realizado com sucesso!")

    else:
        print("O valor informado é inválido.")
    
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido, tente novamente.")
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("----------------Extrato----------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"saldo final: R$ {saldo:.2f}")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
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
                numero_de_saques=numero_de_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            mostrar_extrato (saldo, extrato=extrato)

        elif opcao == "4":
            cadastrar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta_bancaria (AGENCIA,numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)
        
        elif opcao == "0":
            print("Obrigado por usar o sistema!")
            break

        else:
            print("Opção inválida, tente novamente.")

main()

=======
menu = """
Escolha uma opção: 

[1] Depositar 
[2] Sacar 
[3] Extrato 
[0] Sair


A opção escolhida foi:  """ 

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0 
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Valor inválido, tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES 

        if excedeu_saldo:
            print("Você não tem saldo suficiente para reliazar essa operação.")

        elif excedeu_limite:
            print("Valor limite do saque excedido! O valor máximo para cada saque é de até R$500,00")
        
        elif excedeu_saques:
            print("O limite é de até 3 saques por dia.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque R$ {valor:.2f} \n"
            numero_de_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":
        print("----------------Extrato----------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"saldo final: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por usar o sistema!")
        break

    else:
        print("Opção inválida, tente novamente.")
>>>>>>> e22bb7e4df78bb1e4d7f4a7c9dcd65cbe88fb82c
