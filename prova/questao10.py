soma_pares = 0

while True:
    numero = int(input("Digite um número inteiro (ou um número negativo para sair): "))

    if numero < 0:
        break

    soma_pares += numero if numero % 2 == 0 else 0

print("A soma dos números pares digitados é:", soma_pares)