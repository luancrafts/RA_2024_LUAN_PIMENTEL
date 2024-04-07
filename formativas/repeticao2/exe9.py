print("Números primos de 1 a 100:")

for numero in range(2, 101):
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(numero)