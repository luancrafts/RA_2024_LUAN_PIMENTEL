lista=[]
num = 1
tamanho = 0

while num!=0:
    num = int(input("Digite o numero que deseja"))
    lista.append(num)

tamanho = len(lista)
del lista [tamanho-1]

for numero in lista:
    print(numero)