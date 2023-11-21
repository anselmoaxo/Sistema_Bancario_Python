menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == 'd':
        deposito = float(input("Digite o Valor que gostaria de Depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato = f'Deposito : R$ {deposito:.2f}/n'
        else:
            print('Falhou ! Valor digitado menor ou igual a ZERO')

    elif opcao == 's':
        saque = float(input('Digite o Valor que deseja Sacar: '))

        excedeu_saldo = saldo < saque
        excedeu_limite = limite < saque
        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Falhou ! Você não tem Saldo para realizar o Saque!')
        elif excedeu_limite:
            print('Falhou ! Seu Limite é insuficiente para o Saque.')
        elif execedeu_saques:
            print('Falhou ! Seu numero de Saques já foi atindido ')

        elif saque > 0:
            saldo -= saque
            extrato = f'Saque : R$ {saque:.2f}/n'
            numero_saques += 1

    elif opcao == 'e':
        print("\n########### EXTRATO ###########")
        print("Não foram realizadas movimenatações." if not extrato else extrato)
        print(f"\n Saldo R$ {saldo:.2f}")
        print("##################################")

    elif opcao == "q":
        break

    else:
        print('Operação invalida tenta novamente')