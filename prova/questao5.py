# if num %2 == 0
soma = 0
numero = int(input("Digite um numero: "))

while numero<0:
    numero= int(input("Digite um número positivo"))

for i in range (1, numero, 1):
    soma = soma + i

print(f"A soma dos valores é {soma}")