#operações com conjuntos
A = {1,2,3,4,5,6}
B = {0,2,3.4,5,6,7,8}
print (A.union(B))
print (A.intersection(B))
print (len(A))
if 9 in A:
    print("Pertence")
else:
    print("Não pertence")
# complex(3,4) 3+4i (contempla a unidade imaginaria)
# existe também o comando A.remove(2) para remover o elemento 2 do conjunto A
# A está contido em B se    A<=B
# A é subconjunto proprio de B se A<B