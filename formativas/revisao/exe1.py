numero = float(input("Digiete uma nota entre 0 e 10"))
while (numero <0 or numero>10):
    print(f"O numero digitado {numero} é inválido")
    numero = float(input("DIgite um anota entre 0 e 10"))
print(f"O numero {numero} informado é válido")