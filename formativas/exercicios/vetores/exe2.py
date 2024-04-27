vetor = []
opcao = 1

while opcao != 0:
    opcao = int(input("Digite 0 para sair. 1 Para adicionar numero e 2 para remover: "))

    if opcao == 1:
        numero = int(input("Digite o numero desejado: "))
        vetor.append(numero)
        vetor.sort()

    elif opcao == 2:
        numero = int(input("Digite o numero que deseha remover: "))
        if numero in vetor:
            vetor.remove(numero)
            vetor.sort()

for i in vetor:
    print(i)