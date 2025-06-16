vermelho = "\033[31m"
roxo = "\033[35m"
verde = "\033[32m"
def depositar_dinheiro(valor, valido=False, saldo=0):
    while not valido:
        if (valor <= 0):
            print(f"{vermelho}Valor invalido!")
            valor = float(input(f"{roxo}Informe um valor valido: "))
        else:
            valido = True    

    saldo += valor
    print(f"{verde}Deposito efetuado com sucesso! Seu saldo atual é: R${saldo}")
    return True, saldo