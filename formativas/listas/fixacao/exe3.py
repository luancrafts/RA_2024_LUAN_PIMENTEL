i=0
listaa=[]

while i<10:
    numero = int(input("Digite um numero: "))
    listaa.append(numero)
    i = i+1

for numero in listaa:
    print(numero) 

menor_valor = min(listaa)
maior_valor = max(listaa)
print(f" O menor é: {menor_valor}, O maior é: {maior_valor}")
