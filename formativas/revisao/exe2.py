nomeusuario = input("Digite o seu nome de usuario: ")
senhausuario = input("Digite a sua senha: ")
while senhausuario == nomeusuario:
    senhausuario = input(f"Digite uma senha diferente de {nomeusuario}")
print("Nome e senha definidos")