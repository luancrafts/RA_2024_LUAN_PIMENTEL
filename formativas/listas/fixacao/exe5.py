listanova=[]
i=0
num = 0
maior = 0
listamenor = []
somatorio = 0

while i<5:
    numero = int(input("Digite o numero: "))
    listanova.append(numero)
    i= i+1

for num in listanova:
    if num % 2 == 0 and num > maior:
        maior = num
    
    elif num %2 !=0: #perguntar o tendenciar
        listamenor.append(num)

for num in listanova:
    somatorio = somatorio + num

menor = min(listamenor)

media = somatorio /5
print(f"O maior número da lista é: {maior}, O menor é: {menor}, A soma : {somatorio} e a media é: {media}")
