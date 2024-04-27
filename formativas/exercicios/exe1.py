index = 0
vetor = [1,2,3,4,5]
index = int(input("Digite o numero do index que deseha consultar: "))

if index>=0 and index <len(vetor):
    print(vetor[index])
    
else:
    print("O indice fornecido está fora dos limites do vetor.")