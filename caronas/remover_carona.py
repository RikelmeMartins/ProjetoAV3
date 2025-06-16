import main as usuario
caronas = usuario.carona
verde = "\033[32m"
vermelho = "\033[31m"
def remover_carona(data):
    indice = -1
    encontrada = False
    for ind in range(len(caronas)):
        if(data == caronas[ind]["data"]):
            indice = ind
    if(indice == -1):
        print(f"{vermelho}Não encontrou a carona!")
    else:
        print(f"{verde}Carona encontrada!")
        encontrada = True

    return indice, encontrada