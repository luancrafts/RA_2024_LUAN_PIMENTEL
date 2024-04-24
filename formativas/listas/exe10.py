listanomes = ["Joao", "Maria", "Augustinho", "lola", "Palooza"]

tamanho = len(listanomes)
indice = int(input(f"Informe o indice que quer remover entre 0 e {tamanho}"))

del listanomes[indice-1]

for nome in listanomes:
    print(nome)
