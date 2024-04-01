"""
PONTIFICIA UNIVERSIDADE CATOLICA DO PARANÁ
LUAN FELIX PIMENTEL
01.04.2024

ESTE ALGORITMO REALIZA A LEITURA DE SALÁRIO DE UM CONTRIBUINTE E COM BASE EM UMA TABELA ESTABELECIDA
DE VALORES, DETERMINA A FAIXA QUE O CONTRIBUINTE SE ENCONTRA E QUAL VALOR SERÁ DESCONTADO
EM SEU CONTRACHEQUE.
"""

salario_contribuinte=float(input("Informe o valor de seu salário: "))

if salario_contribuinte >= 0 and salario_contribuinte <= 2259.20:
    faixa_atual = "isenta"
    imposto = 0
    print("A sua faixa de renda atual está", faixa_atual, "e o valor a ser descontado em seu contracheque é", imposto)

elif salario_contribuinte >=0 and salario_contribuinte >=2259.21 and salario_contribuinte <= 2826.65:
    faixa_atual = "7,5%"
    imposto = salario_contribuinte*0.075 #de acordo com a tabela
    print("A sua faixa de renda atual é de: ", faixa_atual, "e o valor a ser descontado em seu contracheque é de: R$ ", imposto)

elif salario_contribuinte >= 2826.66 and salario_contribuinte <= 3751.05:
    faixa_atual = "15%"
    imposto = salario_contribuinte*0.15
    print("A sua faixa de renda atual é de: ", faixa_atual, "e o valor a ser descontado em seu contracheque é de: R$ ", imposto)

elif salario_contribuinte >= 3751.06 and salario_contribuinte <= 4664.68:
    faixa_atual = "22,5%"
    imposto = salario_contribuinte*0.225
    print("A sua faixa de renda atual é de: ", faixa_atual, "e o valor a ser descontado em seu contracheque é de: R$ ", imposto)

elif salario_contribuinte > 4664.68:
    faixa_atual = "27,5%"
    imposto = salario_contribuinte*0.275
    print("A sua faixa de renda atual é de: ", faixa_atual, "e o valor a ser descontado em seu contracheque é de: R$ ", imposto)
else:
    print("O valor inserido não é valido.")