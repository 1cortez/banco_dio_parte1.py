saldo = 0
sacar = []
depositar = []
saque = 0
deposito = 0 

while True:


    print("""
BANCO WEILER
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
""")

    opc = int(input("O que iremos fazer? "))
    while opc not in (1, 2, 3, 4):
        print("Insira um valor válido!")
        opc = int(input("O que iremos fazer? "))

    if opc == 1:
        deposito = float(input("Quantos R$ deseja depositar? "))
        saldo += deposito
        print(saldo)
        print(deposito)
        print(f"O seu saldo atual é R${saldo}")
        depositar.append(deposito)
    elif opc == 2:
        if saldo <= 0:
            print("Saldo insuficiente!")
        else: 
            saque = float(input("Quantos R$ deseja sacar? "))
            if saque > saldo:
                print("Valor maior que o seu saldo!")
            else:
                saldo -= saque
                print(f"O seu saldo atual é R${saldo}")
                sacar.append(saque)
    elif opc == 3:
        print(f"Historico de saques {sacar}")
        print(f"Historico de depositos {depositar}")
    elif opc == 4:
        print("FIM DO PROGRAMA!")
        break
            




