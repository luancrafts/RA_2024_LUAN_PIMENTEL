numerototal = int(input("Digite o numero total de eleitores: "))
i = 0
votos1 = 0
votos2 =0
votos3 = 0

while i<numerototal:
    opcao = int(input("Digite o numero do candidato que você quer votar, 1, 2 ou 3: "))
    if opcao == 1:
        votos1 = votos1 +1 
        i= i+1
    
    elif opcao == 2:
        votos2 = votos2 +1 
        i= i+1
    
    elif opcao == 3:
        votos3 = votos3 +1 
        i= i+1
print(f"O total de votos de cada candidato foi: candidato1 {votos1}, candidato2 {votos2}, candidato3 {votos3}")