total_idades = 0

for i in range(1, 6):
    idade = int(input("Digite a idade da pessoa " + str(i) + ": "))
    total_idades += idade

media_idades = total_idades / 5

print("A média das idades é:", media_idades)