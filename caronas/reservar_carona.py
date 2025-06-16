verde = '\033[32m'
vermelho = '\033[31m'
roxo = '\033[35m'

def reserva_carona(reserva, nome, passageiros, vagas, saldo, valor, vagas_ocupadas):
    if (reserva == 'S'):
        if (saldo  < valor):
            print(f"{vermelho}Saldo insuficiente!")
        else:
            print(f"{verde}Vaga reservada!")
            vagas -= 1
            saldo -= valor
            passageiros.append(nome)
            vagas_ocupadas += 1
            input(f"{roxo}Aperte enter para continuar...")
    else:
        print("Vaga não reservada!")
        input(f"{roxo}Aperte enter para continuar...") 