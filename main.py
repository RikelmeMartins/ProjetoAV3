import os
import usuarios.cadastro as cadastro
import validacao.entrada_texto as entrada_texto
import validacao.senha as sen
import validacao.email as en
import validacao.data as data_valida_futura_ou_hoje
import validacao.hora as hora_valida
import caronas.cadastrar_carona as cadastrar_carona
import caronas.reservar_carona as reserva_carona
import caronas.remover_reserva as remover_reserva
import caronas.remover_carona as remover_carona
import emergencia.cadastro_carona_emergencia as caronas_emergencia
import passageiro.deposito as depositar_dinheiro
import manipular_arquivo.resetar_usuarios as resetar_usuarios
import relatorios.reset_relatorio as resetar_relatorio  
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
chave_acesso = '23052005'
caminho = 'ProjetoAV3/manipular_arquivo/usuarios.txt'
caminho_importar = 'ProjetoAV3/manipular_arquivo/import_usuarios.txt'

def menu_principal():
    print(f"{roxo}Escolha uma das opções\n\n"
          "[1] - Cadastro\n"
          "[2] - Login\n"
          "[3] - Importar usuarios\n"
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

def menu_passageiro():
    print(f"{roxo}Escolha uma das opções\n\n"
          "[1] - Lista de caronas disponiveis\n"
          "[2] - Origem e destino\n"
          "[3] - Reserva vaga\n"
          "[4] - Cancelar reserva\n"
          "[5] - Detalhes de carona\n"
          "[6] - Caronas cadastradas\n"
          "[7] - SOS\n"
          "[8] - Depositar dinheiro\n"
          "[9] - Verificar SOS\n"
          "[0] - Logout\n")
    op = input("Opção: ")
    return op

def menu_motorista():
    print(f"{roxo}Escolha uma das opções\n\n"
          "[1] - Cadastro de carona\n"
          "[2] - Remover carona\n"
          "[3] - Verificar caronas cadastradas\n"
          "[4] - SOS\n"
          "[5] - Relatório de corridas\n"
          "[0] - Logout\n")
    op = input("Opção: ")
    return op

def menu_admin():
    print(f"{roxo}Escolha uma das opções\n\n" 
            "[1] - Lista de usuarios\n" 
            "[2] - Remover usuario\n"
            "[0] - Logout\n")
    op = input("Opção: ")
    return op

resetar_usuarios.resetar_usuarios_txt()
resetar_relatorio.resetar_relatorio_txt()
# Início do programa
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{roxo}=" * 130)
    print(f"""{roxo}
 ____  ______ __  __    __      _______ _   _ _____   ____               ____      _____        _____ _______ _____ _    _ _ 
|  _ \|  ____|  \/  |   \ \    / /_   _| \ | |  __ \ / __ \        /\   / __ \    |  __ \ /\   |  __ \__   __|_   _| |  | | |
| |_) | |__  | \  / |    \ \  / /  | | |  \| | |  | | |  | |      /  \ | |  | |   | |__) /  \  | |__) | | |    | | | |  | | |
|  _ <|  __| | |\/| |     \ \/ /   | | | . ` | |  | | |  | |     / /\ \| |  | |   |  ___/ /\ \ |  _  /  | |    | | | |  | | |
| |_) | |____| |  | |      \  /   _| |_| |\  | |__| | |__| |    / ____ \ |__| |   | |  / ____ \| | \ \  | |   _| |_| |__| |_|
|____/|______|_|  |_|       \/   |_____|_| \_|_____/ \____/    /_/    \_\____/    |_| /_/    \_\_|  \_\ |_|  |_____|\____/(_)                                                                                                                                                                                                                  
    """)
    print(f"{roxo}=" * 130)
    opcao = menu_principal()

    if (opcao == '0'):
        print("Saindo...")
        break

    elif(opcao == '1'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{roxo}=" * 60)
        print(f"""{roxo}
   _____          _           _             
  / ____|        | |         | |            
 | |     __ _  __| | __ _ ___| |_ _ __ ___  
 | |    / _` |/ _` |/ _` / __| __| '__/ _ \ 
 | |___| (_| | (_| | (_| \__ \ |_| | | (_) |
  \_____\__,_|\__,_|\__,_|___/\__|_|  \___/                                                                                                                                                                                                               
    """)
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
            if email in passageiros:
                print(f"{vermelho}Email já cadastrado! Tente novamente.")
                email = en.obter_email_valido("Email: ")
            senha = entrada_texto.obter_entrada_valida("Senha: ")
            while not sen.verificar_senha(senha):
                print(f"{vermelho}Senha inválida! Tente novamente.")
                senha = entrada_texto.obter_entrada_valida("Senha: ")
            usuario = cadastro.cadastrar_passageiro(email, nome, senha)
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
            if email in motoristas:
                print(f"{vermelho}Email já cadastrado! Tente novamente.")
                email = en.obter_email_valido("Email: ")
            senha = entrada_texto.obter_entrada_valida("Senha: ")
            while not sen.verificar_senha(senha):
                print(f"{vermelho}Senha inválida! Tente novamente.")
                senha = entrada_texto.obter_entrada_valida("Senha: ")
            usuario = cadastro.cadastrar_motorista(email, nome, senha)
            motoristas.append(usuario)
            print(f"{verde}Cadastro de motorista realizado com sucesso!")
            input(f"{roxo}Aperte enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
           
        elif (op == '3'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de admin!\n")
            print(f"{roxo}Preencha os dados abaixo para cadastrar um admin:\n")
            print(f"{roxo}Para cadastrar um admin, você precisa informar a chave de acesso.")
            acesso = False
            while not acesso:
                entrada = entrada_texto.obter_entrada_valida("Digite a chave de acesso: ")
                if entrada == chave_acesso:
                    acesso = True
                else:
                    print(f"{vermelho}Chave de acesso inválida! Tente novamente.")
            nome = entrada_texto.obter_entrada_valida("Nome: ")
            email = en.obter_email_valido("Email: ")
            if email in admin:
                print(f"{vermelho}Email já cadastrado! Tente novamente.")
                email = en.obter_email_valido("Email: ")
            senha = entrada_texto.obter_entrada_valida("Senha: ")
            while not sen.verificar_senha(senha):
                print(f"{vermelho}Senha inválida! Tente novamente.")
                senha = entrada_texto.obter_entrada_valida("Senha: ")
            usuario = cadastro.cadastrar_admin(email, nome, senha)
            admin.append(usuario)
            print(f"{verde}Cadastro de admin realizado com sucesso!")
            input(f"{roxo}Aperte enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (op == '4'):
            print("Lista de usuários cadastrados:")
            print(f"{roxo}Passageiros: {passageiros}")
            print(f"{roxo}Motoristas: {motoristas}")
            print(f"{roxo}Admins: {admin}")
    elif(opcao == '2'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{roxo}=" * 60)
        print(f"""{roxo}
  _      ____   _____ _____ _   _ 
 | |    / __ \ / ____|_   _| \ | |
 | |   | |  | | |  __  | | |  \| |
 | |   | |  | | | |_ | | | | . ` |
 | |___| |__| | |__| |_| |_| |\  |
 |______\____/ \_____|_____|_| \_|                                                                                                                                                                                                                                       
    """)
        print(f"{roxo}=" * 60)
        print(f"{roxo}Faça seu login!\n")
        usuario_encontrado = False
        emailLogin = en.obter_email_valido("Email: ")
        for p in passageiros:
            if (emailLogin == p["email"]):
                senhaLogin = input(f"{roxo}Informe sua senha: ")
                if (senhaLogin == p["senha"]):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    usuario_encontrado = True
                    print(f"{verde}Login concluido!")
                    print(f"{roxo}\nBem vindo {p["nome"]} ao partiu!\n")
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        op = menu_passageiro()
                        
                        os.system('cls' if os.name == 'nt' else 'clear')
                        op = menu_passageiro()
                        if (op == '0'):
                            break

                        elif(op == '1'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Lista de caronas disponiveis!\n")
                            print(f"{roxo}="*60)
                            for c in caronas:
                                print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                print(f"{roxo}="*60)
                            
                            input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif(op == '2'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Origem e destino!\n")

                            origemBusca = input(f"{roxo}Informe a origem: ")
                            destinoBusca = input(f"{roxo}Informe o destino: ")

                            for c in caronas:
                                if (origemBusca in c["origem"] and destinoBusca in c["destino"]):
                                    print(f"{roxo}\nCarona encontrada!\n")
                                    print(f"{roxo}=" * 60)
                                    print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                    print(f"{roxo}=" * 60)

                                    input(f"{roxo}Aperte enter para continuar...") 
                                else:
                                    print(f"{vermelho}\nNenhuma carona encontrada!\n")
                                    input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif (op == '3'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Reservar vagas!\n")

                            emailBusca = input(f"{roxo}Informe o email do motorista: ")
                            dataBusca = input(f"{roxo}Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                    print(f"{roxo}=" * 60)
                                    print(f"{roxo}\nCarona encontrada!\n")
                                    print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                    
                                    vagas = c["vagas"]
                                    saldo = p["saldo"]
                                    passageiros = c["passageiros"]
                                    nome = p["nome"]
                                    valor = c["valor"]
                                    vagas_ocupadas = c["vagas_ocupadas"]
                                    if (c["vagas"] <= 0):
                                        print(f"{vermelho}Não há vagas disponiveis!")
                                        input(f"{roxo}Aperte enter para continuar...") 
                                        break
                                    
                                    reserva = input(f"{roxo}\nDeseja reserva uma vaga (s/n): ").upper()

                                    reserva_carona.reserva_carona(reserva, nome, passageiros, vagas, saldo, valor, vagas_ocupadas)

                                else:
                                    print(f"{vermelho}\nCarona não encontrada!\n")
                                    input(f"{roxo}Aperte enter para continuar...")
                        elif (op == '4'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Remover reserva!\n")

                            emailBusca = input(f"{roxo}Informe o email do motorista: ")
                            dataBusca = input(f"{roxo}Informe a data da carona: ")

                            for c in caronas:
                                vagas = c["vagas"]
                                saldo = p["saldo"]
                                passageiros = c["passageiros"]
                                nome = p["nome"]
                                valor = c["valor"]
                                vagas_ocupadas = c["vagas_ocupadas"]
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                        print(f"{roxo}=" * 60)
                                        print(f"{verde}\nCarona encontrada!\n")
                                        print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}.")
                                        reserva = input(f"{roxo}\nDeseja remover sua vaga (s/n): ").upper()

                                        remover_reserva.remover_reserva(reserva, saldo, passageiros, vagas, valor, nome)
                                else:
                                    print(f"{vermelho}\nCarona não encontrada!\n")

                        elif(op == '5'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Detalhes da carona!\n")
                            
                            emailBusca = input(f"{roxo}Informe o email do motorista: ")
                            dataBusca = input(f"{roxo}Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                    print(f"{roxo}=" * 60)
                                    print(f"{verde}\nCarona encontrada!\n")
                                    print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}")
                                    input(f"{roxo}Aperte enter para continuar...") 
                                else:
                                    print(f"{vermelho}Carona não encontrada!")
                                    input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif (op == '6'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Caronas Cadastradas!\n")
                            print(f"{roxo}="*60)
                            for c in caronas:
                                print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]},\n"
                                        f"Passageiros: {c["passageiros"]}")
                                print(f"{roxo}="*60)

                            input(f"{roxo}Aperte enter para continuar...") 

                        elif(op == '7'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Corrida de emergência!\n")

                            origem = entrada_texto.obter_entrada_valida("Informe a origem: ")
                            destino = entrada_texto.obter_entrada_valida("Informe o destino: ")
                            data = entrada_texto.obter_entrada_valida("Informe a data (dia/mes/ano): ")
                            dataValida = data_valida_futura_ou_hoje.data_valida_futura_ou_hoje(data)
                            while not dataValida:
                                print(f"{vermelho}Data invalida! Informe uma data futura ou a data de hoje.")
                                data = entrada_texto.obter_entrada_valida("Informe a data (dia/mes/ano): ")
                                dataValida = data_valida_futura_ou_hoje.data_valida_futura_ou_hoje(data)
                            hora = entrada_texto.obter_entrada_valida("Informe o horario aproximado (hora:minutos): ")
                            horaValida = hora_valida.hora_valida(hora)
                            while not horaValida:
                                print(f"{vermelho}Horário inválido! Informe um horário válido (hora:minutos).")
                                hora = entrada_texto.obter_entrada_valida("Informe o horario (hora:minutos): ")
                            motivo = entrada_texto.obter_entrada_valida("Informe o motivo (Opicional): ")
                            caronas_emergencia.caronas_emergencia(p["nome"], p["email"], origem, destino, data, hora, motivo, emergencia)
                            print(f"{verde}Corrida de emergência concluido. Espero um motorista aceitar!")
                            input(f"{roxo}Aperte enter para continuar...") 

                        elif(op == '8'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Depositar dinheiro!\n")
                            saldo = p["saldo"]
                            valor = float(entrada_texto.obter_entrada_valida("Informe o valor do deposito: "))
                            depositar_dinheiro.depositar_dinheiro(valor, True, saldo)
                            input(f"{roxo}Aperte enter para continuar...")

                        elif (op == '9'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Verificar se o chamado foi atendido!\n")

                            for e in emergencia:
                                if (e["atendido"] == True):
                                    print(f"{verde}Sua corrida foi aceita!")
                                    print(f"{roxo}Nome do motorista: {e["motorista"]}")
                                    input(f"{roxo}Aperte enter para continuar...") 
                                else:
                                    print(f"{vermelho}Aguarde mais um pouco!")
                                    input(f"{roxo}Aperte enter para continuar...") 

                        else:
                            print(f"{vermelho}Opção inválida! Tente novamente.")
                            input(f"{roxo}Aperte enter para continuar...") 
                            os.system('cls' if os.name == 'nt' else 'clear')
                            continue
                else:
                    print(f"{vermelho}Senha ou email invalido! Tente novamente.")
                    input(f"{roxo}Aperte enter para continuar...") 
        if not usuario_encontrado:
            for m in motoristas:
                if (emailLogin == m["email"]):
                    senhaLogin = input(f"{roxo}Informe sua senha: ")
                    if (senhaLogin == m["senha"]):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        usuario_encontrado = True
                        print(f"{verde}Login concluido!")
                        print(f"{roxo}\nBem vindo {m["nome"]} ao partiu!\n")
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            op = menu_motorista()
                            if (op == '0'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break

                            elif(op == '1'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Cadastrar uma carona!\n")
                                origem = entrada_texto.obter_entrada_valida("Informe a origem: ")
                                destino = entrada_texto.obter_entrada_valida("Informe o destino: ")
                                data = entrada_texto.obter_entrada_valida("Informe a data (dia/mes/ano): ")
                                dataValida = data_valida_futura_ou_hoje.data_valida_futura_ou_hoje(data)
                                while not dataValida:
                                    print(f"{vermelho}Data invalida! Informe uma data futura ou a data de hoje.")
                                    data = entrada_texto.obter_entrada_valida("Informe a data (dia/mes/ano): ")
                                    dataValida = data_valida_futura_ou_hoje.data_valida_futura_ou_hoje(data)
                                hora = entrada_texto.obter_entrada_valida("Informe o horario (hora:minutos): ")
                                while not hora_valida.hora_valida(hora):
                                    print(f"{vermelho}Horário inválido! Informe um horário válido (hora:minutos).")
                                    hora = entrada_texto.obter_entrada_valida("Informe o horario (hora:minutos): ")
                                vagas = int(entrada_texto.obter_entrada_valida("Informe a quantidade de vagas: "))
                                while vagas <= 0:
                                    print(f"{vermelho}Quantidade de vagas invalida!")
                                    vagas = int(entrada_texto.obter_entrada_valida("Informe a quantidade de vagas: "))
                                valor = float(entrada_texto.obter_entrada_valida("Informe o valor por vaga: "))
                                while valor <= 0:
                                    print(f"{vermelho}Valor invalido!")
                                    valor = float(entrada_texto.obter_entrada_valida("Informe o valor por vaga: "))
                                caronas += 1

                                cadastrar_carona.cadastrar_carona(m["email"], m["nome"], origem, destino, data, hora, vagas, valor, caronas)
                                input(f"{roxo}Aperte enter para continuar...")

                            elif(op == '2'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Remover carona!\n")
                                if m["caronas"] == 0:
                                    print(f"{verde}Nenhuma carona cadastrada!\n")
                                    input(f"{roxo}Aperte enter para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                                dataBusca = entrada_texto.obter_entrada_valida(f"{roxo}Informe a data da carona: ")
                                indice, encontrada = remover_carona.remover_carona(dataBusca)
                                if encontrada:
                                    for c in caronas:
                                        print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                              f"Email do motorista: {c["email"]},\n"
                                              f"Origem: {c["origem"]},\n"
                                              f"Destino: {c["destino"]},\n"
                                              f"Data: {c["data"]},\n"
                                              f"Horario: {c["hora"]},\n"
                                              f"Vagas: {c["vagas"]},\n"
                                              f"Valor por vagas: R${c["valor"]},\n"
                                              f"Passageiros: {c["passageiros"]}")
                                    remover = entrada_texto.obter_entrada_valida("Deseja remover essa carona do sistema (s/n)? ").upper()
                                    if (remover == 'S'):
                                        senhaValidacao = entrada_texto.obter_entrada_valida(f"{roxo}Informe sua senha: ")
                                        if (senhaValidacao == m["senha"]):
                                            print(f"{verde}Carona removida!")
                                            caronas.pop(indice)
                                            input(f"{roxo}Aperte enter para continuar...")
                                        else:
                                            print(f"{vermelho}Senha invalida!")
                                            input(f"{roxo}Aperte enter para continuar...")

                            
                            elif (op == '3'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Caronas cadastradas!\n")
                                encontrada = False
                                if m["caronas"] == 0:
                                    encontrada = True
                                if not encontrada:
                                    print(f"{verde}Nenhuma carona cadastrada!\n")
                                    input(f"{roxo}Aperte enter para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                                    
                                else:
                                    print(f"{roxo}Caronas cadastradas por {m["nome"]}:\n")
                                    for c in caronas:
                                        print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                              f"Email do motorista: {c["email"]},\n"
                                              f"Origem: {c["origem"]},\n"
                                              f"Destino: {c["destino"]},\n"
                                              f"Data: {c["data"]},\n"
                                              f"Horario: {c["hora"]},\n"
                                              f"Vagas: {c["vagas"]},\n"
                                              f"Valor por vagas: R${c["valor"]},\n"
                                              f"Passageiros: {c["passageiros"]}")
                                input(f"{roxo}Aperte enter para continuar...")

                            elif (op == '4'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Corrida de emergencia!\n")

                                for e in emergencia:
                                    print(f"{roxo}Corridas de emergencia registradas!\n")

                                    if (e["atendido"] == True):
                                        print(f"{verde}Nenhuma corrida de emergencia pendente!\n")
                                        input(f"{roxo}Aperte enter para continuar...")
                                        os.system('cls' if os.name == 'nt' else 'clear')

                                    else:
                                        print(f"{roxo}Nome: {e["nome"]},\n"
                                                f"Email: {e["email"]},\n"
                                                f"Origem: {e["origem"]},\n"
                                                f"Destino: {e["destino"]},\n"
                                                f"Data: {e["data"]},\n"
                                                f"Horario: {e["hora"]},\n"
                                                f"Motivo: {e["motivo"]},\n"
                                                f"Atendida: {e["atendido"]},\n"
                                                f"Motorista: {e["motorista"]}")

                                        aceitar = input("Deseija aceitar esse corrida de emergencia (s/n)? ").upper()

                                        if (aceitar == 'S'):
                                            if (e["email"] == email and e["atendido"] == False):
                                                e["atendido"] = True
                                                e["motorista"] = nome
                                                print(f"{verde}Corrida de emergência aceita! Contate o usuario: {e['nome']}, {e['email']}")
                                                input(f"{roxo}Aperte enter para continuar...")
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                
                            elif (op == '5'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Relatório de corridas!\n")
                                total_ganho = 0

                                if m["caronas"] == 0:
                                    print(f"{verde}Nenhuma corrida realizada!\n")
                                    input(f"{roxo}Aperte enter para continuar...")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    
                                else:
                                    for c in caronas:
                                        if (c["email"] == m["email"]):
                                            total_ganho += c["vagas_ocupadas"] * c["valor"]
                                    print(f"{roxo}Caronas realizadas por {m["nome"]}:\n")
                                    print(f"{roxo}=" * 60)
                                    for c in caronas:
                                        if (c["email"] == m["email"]):
                                            print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                                    f"Email do motorista: {c["email"]},\n"
                                                    f"Origem: {c["origem"]},\n"
                                                    f"Destino: {c["destino"]},\n"
                                                    f"Data: {c["data"]},\n"
                                                    f"Horario: {c["hora"]},\n"
                                                    f"Vagas restantes: {c["vagas"] - c["passageiros"]},\n"
                                                    f"Valor por vagas: R${c["valor"]}."
                                                    f"{roxo}Total ganho: R${total_ganho:.2f}")
                                            print(f"{roxo}=" * 60)
                                    
                                    salvar = input(f"{roxo}Deseja salvar esse relatório (s/n)? ").upper()
                                    caminho_relatorio = "ProjetoAV3/relatorios/relatorio.txt"
                                    if (salvar == 'N'):
                                        print(f"{roxo}Relatório não salvo!")
                                        input(f"{roxo}Aperte enter para continuar...")
                                    if (salvar == 'S'):
                                        with open(caminho_relatorio, "w") as f:
                                            f.write(f"Relatório de corridas de {m['nome']}:\n")
                                            f.write(f"Total ganho: R${total_ganho:.2f}\n")
                                            f.write(f"Caronas realizadas:\n")
                                            for c in caronas:
                                                f.write(f"Nome do motorista: {c['nome']},\n"
                                                        f"Email do motorista: {c['email']},\n"
                                                        f"Origem: {c['origem']},\n"
                                                        f"Destino: {c['destino']},\n"
                                                        f"Data: {c['data']},\n"
                                                        f"Horario: {c['hora']},\n"
                                                        f"Vagas restantes: {c['vagas'] - c['passageiros']},\n"
                                                        f"Valor por vagas: R${c['valor']}.\n"
                                                        f"Total ganho: R${total_ganho:.2f}\n")
                                            print(f"{verde}Relatório salvo com sucesso!")
                                    input(f"{roxo}Aperte enter para continuar...")

                    else:
                        print(f"{vermelho}Senha ou email invalido! Tente novamente.")
                        input(f"{roxo}Aperte enter para continuar...") 
        if not usuario_encontrado:
            for a in admin:
                if (emailLogin == a["email"]):
                    senhaLogin = input(f"{roxo}Informe sua senha: ")
                    if (senhaLogin == a["senha"]):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        usuario_encontrado = True
                        print(f"{verde}Login concluido!")
                        print(f"{roxo}\nBem vindo {a["nome"]} ao partiu!\n")
                        while True:
                            
                            os.system('cls' if os.name == 'nt' else 'clear')
                            op = menu_admin()

                            if (op == '0'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break

                            elif (op == '1'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Lista de usuarios!\n")
                                print(f"{roxo}=" * 60)
                                print(f"{azul}Passageiros!\n")
                                for usu in passageiros: 
                                    print(f"{azul}Nome: {usu["nome"]}")
                                    print(f"{azul}Email: {usu["email"]}")    
                                print(f"{roxo}=" * 60)
                                print(f"{azul}Motoristas!\n") 
                                for mot in motoristas: 
                                    print(f"{azul}Nome: {mot["nome"]}")
                                    print(f"{azul}Email: {mot["email"]}")  
                                
                                input(f"{roxo}Aperte enter para continuar...")
                            elif (op == '2'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Remover um usuario!\n")
                                emailBusca = input(f"{roxo}Digite o email para buscar: ")
                                indice = -1
                                for ind in range(len(passageiros)):
                                    if(emailBusca == passageiros[ind]["email"]):
                                        indice = ind
                                    if(indice == -1):
                                        print(f"{vermelho}Não encontrou o usuário!")
                                        input(f"{roxo}Aperte enter para continuar...") 
                                    else:
                                        print(f"{verde}Passageiro removido!")
                                        passageiros.pop(indice)
                                        input(f"{roxo}Aperte enter para continuar...")
                                for ind in range(len(motoristas)):
                                    if(emailBusca == motoristas[ind]["email"]):
                                        indice = ind
                                    if(indice == -1):
                                        print(f"{vermelho}Não encontrou o usuário!")
                                        input(f"{roxo}Aperte enter para continuar...") 
                                    else:
                                        print(f"{verde}Motorista removido!")
                                        motoristas.pop(indice)
                                        input(f"{roxo}Aperte enter para continuar...") 
                    else:
                        print(f"{vermelho}Senha ou email invalido! Tente novamente.")
                        input(f"{roxo}Aperte enter para continuar...")

    elif (op == '3'):
        print(f"{roxo}Importar usuários!\n")
        try:
            with open(caminho_importar, "r") as f:
                for linha in f:
                    email, nome, senha, tipo = linha.strip().split(",")
                    if tipo == "passageiro":
                        passageiros.append({"email": email, "nome": nome, "senha": senha, "saldo": 0.0})
                    elif tipo == "motorista":
                        motoristas.append({"email": email, "nome": nome, "senha": senha, "caronas": 0})
            print(f"{verde}Usuários importados com sucesso!")
        except Exception as e:
            print(f"{vermelho}Erro ao importar usuários: {e}")
    else:
        print(f"{vermelho}Opção inválida! Tente novamente.")