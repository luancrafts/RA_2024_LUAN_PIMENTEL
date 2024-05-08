# 1 numpy
#2 c) np.eye(3)
#3) d) np.dot
#4) a) transpose
#5) D

#1)
import numpy as np
n = 3
matriz = [
    [1 if i == j else 0 for j in range(n)]
    for i in range(n)
]

for linha in matriz:
    print(linha)

#2
import numpy as np
A = [[i + j for j in range(2)] for i in range(2)]
B = [[i - j for j in range(2)] for i in range(2)]
resultado = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

for linha in resultado:
    print(linha)

#3
import numpy as np

A = np.array([[i - j for j in range(2)] for i in range(3)])
AT = np.transpose(A)

print(AT)

#4
import numpy as np

A = np.array([[i - j for j in range(3)] for i in range(2)])
B = np.array([[i + j for j in range(3)] for i in range(2)])

resultado = A - B
print(resultado)

#5
import numpy as np

matriz = np.array([[i ** 2 for i in range(4)] for _ in range(4)])
print(matriz)
