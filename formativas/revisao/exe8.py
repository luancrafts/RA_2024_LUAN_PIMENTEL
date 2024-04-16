nome = input("Digite o nome (maior que 3 caracteres): ")
idade = int(input("Digite a idade (entre 0 e 150): "))
salario = float(input("Digite o salário (maior que zero): "))
sexo = input("Digite o sexo ('f' para feminino, 'm' para masculino): ").lower()
estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()

if len(nome) <= 3 or idade < 0 or idade > 150 or salario <= 0 or sexo not in ['f', 'm'] or estado_civil not in ['s', 'c', 'v', 'd']:
    print("Alguma informação fornecida é inválida. Por favor, verifique os critérios e tente novamente.")

else:
    print("Informações válidas:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Salário:", salario)
    print("Sexo:", sexo)
    print("Estado Civil:", estado_civil)
