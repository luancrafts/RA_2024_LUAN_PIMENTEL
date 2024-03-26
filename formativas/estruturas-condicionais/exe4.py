
# Leitura dos 3 lados
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica o tipo do triangulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # equilatero
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero")
    # isosceles
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles")
    # Se não for nenhum dos casos anteriores, é escaleno
    else:
        print("O triângulo é escaleno")
else:
    print("Não foi possível formar um triângulo com os dados fornecidos")