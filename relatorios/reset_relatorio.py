caminho = "ProjetoAV3/relatorios/relatorio.txt"
def resetar_relatorio_txt():
    with open(caminho, "w") as f:
        f.write("")