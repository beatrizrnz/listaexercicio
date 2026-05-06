login_correto = "bia"
senha_correta = "1207"

login = input("Digite o login: ")
senha = input("Digite a senha: ")
if login == login_correto and senha == senha_correta:
    print("Você está logado")
else:
    print("Login ou senha incorretos")