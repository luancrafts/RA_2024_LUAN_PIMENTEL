# Leitura
salario = float(input("Digite o salário anual da pessoa: R$"))

# Condicional
if salario <= 20000:
    aliquota = 0
elif salario <= 50000:
    aliquota = 15
else:
    aliquota = 25

# imposto
imposto = salario * (aliquota / 100)

# escreve
print("Salário anual: ", salario)
print("Alíquota: ", aliquota)
print("Valor do imposto: ", imposto)