numero = int(input("Digite um número: "))

while numero != 0:
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
    numero = int(input("Digite outro número (ou 0 para sair): "))