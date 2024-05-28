myDict = {
    "nome":"Augusto",
    "idade":32,
    "cidade":"Curitiba"
}

print(myDict["nome"])
myDict["estado"]="Paraná"
print(myDict["estado"])

#Aqui faz uma iteração para as chaves
for key in myDict:
    print(key)

#Aqui faz uma iteração para os conteúdos
for key in myDict:
    print(myDict[key])

if "nome" in myDict:
    print(f"nome cadastrado é: ", myDict["nome"])