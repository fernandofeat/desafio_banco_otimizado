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