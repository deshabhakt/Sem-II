import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

eign_val, eign_vec = np.linalg.eig(A)

print(eign_val)
print()
print(eign_vec)

x = np.matmul(A,eign_vec[:,0])
y = eign_val[0]*eign_vec[:,0]
print()

print(x)


print(y)
