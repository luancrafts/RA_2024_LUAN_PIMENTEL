#printar como aspas triplas
suaLista=["laranja", "melancia", "abacaxi", "mamao", "limao"]
i=0

while i<5:
    print (suaLista[i])
    i=i+1

suaLista[2] = "trocafeita"
suaLista.append("finaldalista")

for fruta in suaLista:
    print(fruta)