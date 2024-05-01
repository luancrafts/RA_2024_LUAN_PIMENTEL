import numpy as np

k = 2
a = np.array([[1,2,3],[4,5,6]])
b = np.zeros((6,6))
c = np.ones((3,2))
d = np.eye(3)
e = np.array([[4,5,6],[7,8,9]])
soma = a+e
sub = a-e
elemento = a[1][2]
#multi = k* soma
#multi = np.dot(a,e)
#transposta = a.T
d[0][0] = 9
print(soma)
#print(multi)
#print(f"O elemento é:{elemento}")