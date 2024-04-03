"""
incremento seria: 
- ter uma variavel a mais para acumular as medias
- Adicionar esta variavel no loop
- imprimir a media dos 50 alunos fora e ao fim do loop
"""

con = 0 #Inicialize o contador de alunos
acumulador = 0

while(con < 50):
    n1 = float(input("Entre com a primeira nota: "))
    n2 = float(input("Entre com a segunda nota: "))
    n3 = float(input("Entre com a terceira nota: "))
    n4 = float(input("Entre com a quarta nota: "))

    #Calcula a média anual das notas
    MA = (n1 + n2 + n3 +n4)/4
    acumulador = acumulador + MA #acumulador+=MA
    #Imprime a média
    print("Média anual: ", MA)

    #Verifica se o aluno foi aprovado com base na média
    if(MA>= 7):
        print("Aluno aprovado. Parabéns")
    else:
        print("Aluno Reprovado")
        con+= 1 #Incrementa
        
acumulador = acumulador/50
print("A média das médias é:", acumulador)