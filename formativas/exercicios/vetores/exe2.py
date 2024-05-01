vetor = []
opcao = 1

while opcao != 0:
    opcao = int(input("\n MENU \n 0 para sair \n 1 Para adicionar numero \n 2 para remover \n Digite a opção: "))

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