
# successive over-relaxation (SOR)

import numpy as np
import copy 

# Implementation of successive over-relaxation
def solving(A,X,b,w,i,X_prev):
    tmp = 0
    n = len(A)
    for j in range(n):
        if(i!=j):
            tmp += A[i][j]*X[j]
    
    x =(1-w)*X_prev[i] + w*((b[i] - tmp)/A[i][i])
    
    return x

def SOR(A,X,b,n,w):
    condition = True
    count = 1
    
    accuracyReached = np.array([0.,0.,0.])

    while condition:
        X_prev = copy.copy(X)
        X_new = np.zeros((n))
        for i in range(n):
            for j in range (i):
                X[j] = copy.copy(X_new[j])
            X_new[i] = solving(A,X,b,w,i,X_prev)
            
        
        print(f'\niteration = {count}',end="\t")
        for i in range(n):
            print(f'  X{i+1} = {X_new[i]:.20f}', end = "\t")
        print()
        
        for i in range(n):
            accuracyReached[i] = abs(X_new[i] - X_prev[i]) 
        
        count += 1
        condition = False
        for i in range(n):
            X[i] = copy.copy(X_new[i])
            if accuracyReached[i]>e:
                condition = True

    print('\nSolution:')
    for i in range(n):
        print(f'x{i+1} = {X[i]}', end = "\t")
    print()


n=3

# Coefficient Matrix
A = np.array([
    [4.,3.,0.],
    [3.,4.,-1.],
    [0.,-1.,4.]
    ])

b = np.array([
    [24.],
    [30.],
    [-24.]
    ])

# A = np.array([[3.0,-2.,1.],[1.,-6.,8.],[2.,3.,-6.]])

# b = np.array([
#     [3.],
#     [2.],
#     [1.]
# ])

# A = np.array([[3.,-1.,1.],
#             [-1.,3.,-1.],
#             [1.,-1.,3]
#             ])
# b = np.array([
#     [-1.],
#     [7.],
#     [-7.]
# ])

# initial Guesses
X = np.array([0.,0.,0.])

# Reading tolerable error
e = 0.0001


# Reading relaxation factor
# w = float(input("Enter relaxation factor: "))
w = 0.5

SOR(A,X,b,n,w)















# condition = True
# count = 1
# print(f'\nRelaxation Factor = {w}')
# print('\n(Count, x, y, z)\n')

# while condition:
    
#     x1 = (1-w) * x0 + w * f1(x0,y0,z0)
#     y1 = (1-w) * y0 + w * f2(x1,y0,z0)
#     z1 = (1-w) * z0 + w * f3(x1,y1,z0)

#     print('(%d, %0.20f, %0.20f, %0.20f)\n' %(count, x1,y1,z1))
    
#     e1 = abs(x0-x1)
#     e2 = abs(y0-y1)
#     e3 = abs(z0-z1)
    
#     count += 1
#     x0 = x1
#     y0 = y1
#     z0 = z1
    
#     condition = e1>e and e2>e and e3>e

# print('\nSolution: x = %0.3f, y = %0.3f and z = %0.3f\n'% (x1,y1,z1))