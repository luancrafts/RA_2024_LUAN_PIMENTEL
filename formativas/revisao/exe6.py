inicio = int(input("Digite o primeiro numero: "))
fim = int(input("Digite o segundo numero: "))
soma = 0

if inicio<fim:
    for i in range (inicio+1, fim, 1):
        soma = soma+i
        print(soma)
elif inicio>fim:
    for i in range (fim+1, inicio, 1):
        soma = soma+i
        print(soma)