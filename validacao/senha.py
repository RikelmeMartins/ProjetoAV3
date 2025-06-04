vermelho = '\033[91m'
def verificar_senha(senha):
    if len(senha) < 6:
        print(f"{vermelho}Senha deve ter no minimo 6 caracteres!")
        return False
    if len(senha) > 20:
        print(f"{vermelho}Senha deve ter no maximo 20 caracteres!")
        return False
    return True