# Leitura
atual = float(input("Informe o salário atual: "))
tempo = int(input("Informe em anos o tempo de serviço: "))

# Condicional
if tempo > 5:
    bonus = atual * 0.05  # Calcula o valor do bônus (5% do salário)
    salario = atual + bonus  # Calcula o novo salário com o bônus
    print("Foi recebido um bônus de", bonus,"O novo valor é: ", salario)
else:
    print("Você não tem direito a bônus neste momento.")