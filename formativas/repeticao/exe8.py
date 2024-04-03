x = int(input("Digite um número inteiro positivo: "))
a, b = 0, 1
cont = 0

fibonacci_sequence = []
while cont < x:
    fibonacci_sequence.append(a)
    proximo = a + b
    a = b
    b = proximo
    cont += 1

print(f"Os primeiros", x, "termos da sequência de Fibonacci são:")
print(fibonacci_sequence)