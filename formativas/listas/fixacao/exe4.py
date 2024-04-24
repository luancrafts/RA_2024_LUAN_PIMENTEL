quantidade = int(input("Informe a quantidade de alunos: "))
i=0
listanotas=[]
na_media = 0
notas = 0
abaixo = 0

while i<quantidade:
    nota = int(input("Digite a nota: "))
    listanotas.append(nota)
    i=i+1

for notas in listanotas:
    if notas >= 60:
        na_media = na_media+1
    else:
        abaixo = abaixo+1

print(f"A quantidade alunos acima da média é: {na_media}")
print(f"A quantidade de alunos abaixo da média é: {abaixo}")