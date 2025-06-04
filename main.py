import os
import usuarios.cadastro as cadastro
import validacao.entrada_texto as entrada_texto
import validacao.senha as sen
import validacao.email as en
usuarios = list()
passageiros = list()
motoristas = list()
admin = list()
caronas = list()
emergencia = list()
roxo = '\033[95m'
verde = '\033[92m'
vermelho = '\033[91m'
azul = '\033[94m'

def menu_principal():
    print(f"{roxo}Escolha uma das opções\n\n"
          "[1] - Cadastro\n"
          "[2] - Login\n"
          "[0] - Sair\n")
    op = input("Opção: ")
    return op

def menu_cadastro():
    print(f"{roxo}Escolha uma das opções\n\n"
          "[1] - Passageiro\n"
          "[2] - Motorista\n"
          "[3] - Admin\n"
          "[0] - Sair\n")
    op = input("Opção: ")
    return op
# Início do programa
while True:
    bemvindo = f"""{roxo}
 ____  ______ __  __    __      _______ _   _ _____   ____               ____      _____        _____ _______ _____ _    _ _ 
|  _ \|  ____|  \/  |   \ \    / /_   _| \ | |  __ \ / __ \        /\   / __ \    |  __ \ /\   |  __ \__   __|_   _| |  | | |
| |_) | |__  | \  / |    \ \  / /  | | |  \| | |  | | |  | |      /  \ | |  | |   | |__) /  \  | |__) | | |    | | | |  | | |
|  _ <|  __| | |\/| |     \ \/ /   | | | . ` | |  | | |  | |     / /\ \| |  | |   |  ___/ /\ \ |  _  /  | |    | | | |  | | |
| |_) | |____| |  | |      \  /   _| |_| |\  | |__| | |__| |    / ____ \ |__| |   | |  / ____ \| | \ \  | |   _| |_| |__| |_|
|____/|______|_|  |_|       \/   |_____|_| \_|_____/ \____/    /_/    \_\____/    |_| /_/    \_\_|  \_\ |_|  |_____|\____/(_)                                                                                                                                                                                                                  
    """
    bemvindoCenter = bemvindo.center(80)
    print(f"{roxo}=" * 80)
    print(bemvindoCenter)
    print(f"{roxo}=" * 80)

    opcao = menu_principal()

    if (opcao == '0'):
        print("Saindo...")
        break

    elif(opcao == '1'):
        os.system('cls' if os.name == 'nt' else 'clear')
        bemvindo = f"""{roxo}
   _____          _           _             
  / ____|        | |         | |            
 | |     __ _  __| | __ _ ___| |_ _ __ ___  
 | |    / _` |/ _` |/ _` / __| __| '__/ _ \ 
 | |___| (_| | (_| | (_| \__ \ |_| | | (_) |
  \_____\__,_|\__,_|\__,_|___/\__|_|  \___/                                                                                                                                                                                                               
    """
        bemvindoCenter = bemvindo.center(60, " ")
        print(f"{roxo}=" * 60)
        print(bemvindoCenter)
        print(f"{roxo}=" * 60)

        op = menu_cadastro()

        if (opcao == '0'):  
            print("\nSaindo...")
            os.system('cls' if os.name == 'nt' else 'clear')     
            break

        elif (op == '1'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de passageiros!\n")
            print(f"{roxo}Preencha os dados abaixo para cadastrar um passageiro:\n")
            nome = entrada_texto.obter_entrada_valida("Nome: ")
            email = en.obter_email_valido("Email: ")
            senha = entrada_texto.obter_entrada_valida("Senha: ")
            while not sen.verificar_senha(senha):
                print(f"{vermelho}Senha inválida! Tente novamente.")
                senha = entrada_texto.obter_entrada_valida("Senha: ")
            usuario = cadastro.cadastrar_passageiro(nome, email, senha)
            passageiros.append(usuario)
            print(f"{verde}Cadastro de passageiro realizado com sucesso!")
            input(f"{roxo}Aperte enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (op == '2'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de motoristas!\n")
            print(f"{roxo}Preencha os dados abaixo para cadastrar um motorista:\n")
            nome = entrada_texto.obter_entrada_valida("Nome: ")
            email = en.obter_email_valido("Email: ")
            senha = entrada_texto.obter_entrada_valida("Senha: ")
            while not sen.verificar_senha(senha):
                print(f"{vermelho}Senha inválida! Tente novamente.")
                senha = entrada_texto.obter_entrada_valida("Senha: ")
            usuario = cadastro.cadastrar_motorista(nome, email, senha)
            motoristas.append(usuario)
            print(f"{verde}Cadastro de motorista realizado com sucesso!")
            input(f"{roxo}Aperte enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
           
        
        elif (op == '3'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de admin!\n")
            print(f"{roxo}Preencha os dados abaixo para cadastrar um admin:\n")
            nome = entrada_texto.obter_entrada_valida("Nome: ")
            email = en.obter_email_valido("Email: ")
            senha = entrada_texto.obter_entrada_valida("Senha: ")
            while not sen.verificar_senha(senha):
                print(f"{vermelho}Senha inválida! Tente novamente.")
                senha = entrada_texto.obter_entrada_valida("Senha: ")
            usuario = cadastro.cadastrar_admin(nome, email, senha)
            admin.append(usuario)
            print(f"{verde}Cadastro de admin realizado com sucesso!")
            input(f"{roxo}Aperte enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
