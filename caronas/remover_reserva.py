verde = '\033[32m'
vermelho = '\033[31m'
roxo = '\033[35m'
def remover_reserva(reserva, saldo, passageiros, vagas, valor, nome, vagas_ocupadas):
    if (reserva == 'S'):
        if (saldo < valor):
            print(f"{vermelho}Saldo insuficiente!")
        else:
            print(f"{verde}Reserva cancelada!")
            vagas += 1
            saldo += valor
            passageiros.remove(nome)
            vagas_ocupadas -= 1
            input(f"{roxo}Aperte enter para continuar...")
    else:
        print("Reserva não cancelada!")
        input(f"{roxo}Aperte enter para continuar...")