print("""
----------Cliente por favor insira seus dados a seguir------------""")
print()
nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
nconta = int(input("Digite seu número de conta: "))
idade = int(input("Digite sua idade: "))





menu =  f"""
------Bem vindos ao sistema do banco Y, {nome}, numero de conta:{nconta}---------
--------------------------O que você deseja hoje---------------------------------

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

if idade >=17: 
    print("Você Não tem idade para obter conta em banco")
    
else:

    while True:

        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print(f"Caro cliente {nome.title} a sua Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print(f" Caro cliente {nome.title}, a sua Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print(f" Caro cliente {nome.title}, a sua Operação falhou! Número máximo de saques excedido., tente novamente amanhã")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print(f" Caro cliente {nome.title},Operação falhou! O valor informado é inválido.")

        elif opcao == "3":
            print("\n================ EXTRATO ================")
            print(f" Caro cliente {nome.title} Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
print()
print(f"""     Obrigado(a) por utilizar o Banco Y, tenha um otimo dia Sr(a) {nome.title} {sobrenome.title}  """ )

