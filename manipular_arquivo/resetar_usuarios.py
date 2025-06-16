caminho = "ProjetoAV3/manipular_arquivo/usuarios.txt"
def resetar_usuarios_txt():
    with open(caminho, "w") as f:
        f.write("")