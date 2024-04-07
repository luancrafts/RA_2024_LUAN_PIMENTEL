soma = 0
contador = 0

print("Por favor, insira 5 números:")

while contador < 5:
    numero = float(input(f"Insira o {contador + 1}º número: "))
    soma += numero
    contador += 1

media = soma / 5

print(f"A média dos números inseridos é: {media}")