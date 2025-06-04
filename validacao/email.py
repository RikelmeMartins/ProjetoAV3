def obter_email_valido(mensagem):
    while True:
        email = input(mensagem).strip()
        if email.endswith("@gmail.com"):
            return email
        print("Email inválido! O email deve terminar com '@gmail.com'.")