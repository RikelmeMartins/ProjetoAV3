verde = '\033[32m'
def caronas_emergencia(nome, email, origem, destino, data, hora, motivo, emergencia):
    dadosEmergencia = {
        'nome': nome,
        'email': email,
        'origem': origem,
        'destino': destino,
        'data': data,
        'hora': hora,
        'motivo': motivo,
        'motorista': '',
        'atendido': False
    }
    emergencia.append(dadosEmergencia)
    print(f"{verde}Corrida de emergência cadastrada com sucesso!")