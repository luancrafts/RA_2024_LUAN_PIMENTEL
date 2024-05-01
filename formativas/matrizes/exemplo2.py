import numpy as np

 #Dimensões da matriz
linhas = 2
colunas = 4

#iniciando uma matriz vazia
matriz = []

#Preenchendo a matriz com entrada do usuário
for i in range (linhas):    
    linha =[]
    for j in range (colunas):
        elemento = float(input("Digite o elemento para a posição i e j: "))
        linha.append(elemento)
    matriz.append(linha)

#Convertendo a lista de listas em matriz Numpy
matriz_np = np.array(matriz)
print(matriz_np)