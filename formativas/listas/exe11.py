listanumeros = [1,2,3,4,5]

numero = int(input("Digite o numero que quer remover: "))

while True:
    listanumeros.remove(numero)
    break

for num in listanumeros:
    print(num)