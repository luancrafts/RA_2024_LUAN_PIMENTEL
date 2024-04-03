x = input(int("Forneça um numero inteiro positivo: "))
if x < 0:
    print("O número digitado não é positivo.")
else:
    fatorial = 1
    for i in range(1, x + 1):
        fatorial *= i
    print("O fatorial de ", x, "é ", fatorial)