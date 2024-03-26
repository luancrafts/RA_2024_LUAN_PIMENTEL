# Leitura
nota = float(input("Informe a nota: "))

# Condicional
if nota >= 9.0 and nota <= 10.0:
    classificacao = "A"
elif nota >= 7.0 and nota < 9.0:
    classificacao = "B"
elif nota >= 5.0 and nota < 7.0:
    classificacao = "C"
else:
    classificacao = "D"

# Escreve
print("A sua classificação é: ", classificacao)