numero = int(input("Digite um número inteiro positivo maior que 1: "))

if numero <= 1:
    print("O número fornecido não é válido.")
elif all(numero % i != 0 for i in range(2, int(numero**0.5) + 1)):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")