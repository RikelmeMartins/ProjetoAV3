caminho = 'ProjetoAV3/manipular_arquivo/usuarios.txt'

def cadastrar_passageiro(email, nome, senha):
    usuario = {
        'email': email,
        'nome': nome,
        'senha': senha,
        'saldo': 0
    }
    dados = f"{usuario['email']},{usuario['nome']},{usuario['senha']},{usuario['saldo']}\n"
    with open(caminho, 'a') as arquivo:
        arquivo.write(dados)

    return usuario

def cadastrar_motorista(email, nome, senha):
    usuario = {
        'email': email,
        'nome': nome,
        'senha': senha,
        'caronas': 0
    }
    dados = f"{usuario['email']},{usuario['nome']},{usuario['senha']},{usuario['caronas']}\n"
    with open(caminho, 'a') as arquivo:
        arquivo.write(dados)
        
    return usuario

def cadastrar_admin(email, nome, senha):
    usuario = {
        'email': email,
        'nome': nome,
        'senha': senha
    }
    dados = f"{usuario['email']},{usuario['nome']},{usuario['senha']},{usuario['saldo']}\n"
    with open(caminho, 'a') as arquivo:
        arquivo.write(dados)

    return usuario
