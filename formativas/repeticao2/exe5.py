listafatorial = []
numero = int(input("Digite o numero: "))
cont = numero

while cont >=1:
    listafatorial.append(cont)
    print(listafatorial)
    cont-=1

multi = 1
for e in listafatorial:
    multi = multi * e

print(multi)