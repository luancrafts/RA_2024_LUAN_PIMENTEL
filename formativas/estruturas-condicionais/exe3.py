# Leitura de letra
letra = input("Digite uma letra: ")

# Verifica se a letra é uma vogal utilizando o operador lógico OU (OR)
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("A letra ", letra," é uma vogal")
else:
    print("A letra ", letra," é uma consoante")