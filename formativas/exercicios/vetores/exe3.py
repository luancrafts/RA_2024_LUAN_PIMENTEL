vetor = []
opcao = 1
soma = 0

while opcao != 0:
    opcao = int(input("Digite a opção desejada. 0 Sair, 1 adicionar numero: "))
    if opcao == 1:
        numero = int(input("Digite o número: "))
        vetor.append(numero)
    elif opcao == 0:
        break

for i in vetor:
    soma = soma +i

print(soma)