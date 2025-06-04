def obter_entrada_valida(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print("Entrada inválida! Tente novamente.")