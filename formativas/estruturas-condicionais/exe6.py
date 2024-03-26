# Leitura
compra = float(input("Digite o valor: "))

# Condicional de calculo
if compra > 100.00:
    desconto = compra * 0.10  # Calcula o valor do desconto (10% do valor da compra)
    valor_total = compra - desconto  # Calcula o novo valor total com o desconto
    print("Desconto de ", desconto,"O valor a pagar é: ", valor_total)
else:
    print("Você não tem direito a desconto neste momento")