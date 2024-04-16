numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero"))

numeromaior = numero1
if numero2>numeromaior:
    numeromaior = numero2
if numero3>numeromaior:
    numeromaior = numero3

print(f"O número maior entre {numero1}, {numero2} e {numero3} é: {numeromaior}")