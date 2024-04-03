con = 1
x = int(input("Insira um número inteiro positivo: "))
acumulador = 0

while(con <= x):
   if(con % 2 == 0):
      acumulador+=con
print("O valor acumulado é: ", acumulador)
