x = int(input("Forneça um inteiro positivo maior que 1: "))
primo = True
if x <= 1:
    primo = False
else:
    for i in range(2, x):
        if x % i == 0:
            primo = False
            break
if primo:
    print(x," é um número primo.")
else:
    print(x," não é um número primo.")