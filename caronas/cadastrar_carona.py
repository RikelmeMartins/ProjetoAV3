verde = '\033[32m'
def cadastrar_carona(email, nome, origem, destino, data, hora, vagas, valor, caronas, vagas_ocupadas):
    dadosCarona = {
        'email': email,
        'nome': nome,
        'origem': origem,
        'destino': destino,
        'data': data,
        'hora': hora,
        'vagas': vagas,
        'valor': valor,
        'passageiros': [],
        'caronas': caronas,
        'vagas_ocupadas': 0
    }
    caronas.append(dadosCarona)
    print(f"{verde}Carona cadastrada com sucesso!")