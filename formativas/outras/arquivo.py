nome_do_arquivo = "lista_de_compras.txt"
lista_de_compras = []

while True:
    print("1. Adicionar item à lista")
    print("2. Alterar um item da lista")
    print("3. Remover um item da lista")
    print("4. Salvar o .TXT e sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite o item que deseja adicionar: ")
        lista_de_compras.append(item)

    elif opcao == '2':
        indice = int(input("Digite o número do item que deseja alterar: "))
        novo_item = input("Digite o novo item: ")
        if 0 <= indice < len(lista_de_compras):
            lista_de_compras[indice] = novo_item
        else:
            print("Número inválido.")

    elif opcao == '3':
        indice = int(input("Digite o número do item que deseja remover: "))
        if 0 <= indice < len(lista_de_compras):
            del lista_de_compras[indice]
        else:
            print("Número inválido.")

    elif opcao == '4':
        with open(nome_do_arquivo, 'w') as arquivo:
            for item in lista_de_compras:
                arquivo.write(str(item) + '\n')
        print("Lista salva no arquivo. Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
