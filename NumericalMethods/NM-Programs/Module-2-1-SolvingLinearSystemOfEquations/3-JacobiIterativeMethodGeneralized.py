import numpy as np
import copy


def solving(A,X,b,i):
    tmp = 0
    for j in range(n):
        if(i!=j):
            tmp += A[i][j]*X[j]
    
    x = (b[i] - tmp)/A[i][i]
    return x

# Implementation of Jacobi Iteration

def jacobiMethod(A,X,b,n):

    condition = True
    count = 1
    
    accuracyReached = np.array([0.,0.,0.])

    while condition:

        X_new = np.zeros((n))
        for i in range(n):
            X_new[i] = solving(A,X,b,i)
        
        print(f'\niteration = {count}',end="\t")
        for i in range(n):
            print(f'   X{i+1} = {X_new[i]:.20f}', end = "\t")
        print()
        
        for i in range(n):
            accuracyReached[i] = abs(X_new[i] - X[i]) 
        
        count += 1
        condition = False
        for i in range(n):
            X[i] = X_new[i]
            if accuracyReached[i]>e:
                condition = True

    print(f'\nSolution: Iteration = {count}')
    for i in range(n):
        print(f'x{i+1} = {X[i]}', end = "\t")
    print()


# Initial setup

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

A = np.array([[3.0,-2.,1.],[1.,-6.,8.],[2.,3.,-6.]])

b = np.array([
    [3.],
    [2.],
    [1.]
])

A = np.array([[-10.,-8.,0.],
            [-8.,10.,-1.,],
            [0.,-1.,10.]
            ])

b = np.array([[-6.],[9.],[28.]])

# initial Guesses
X = np.array([0.,0.,0.])

# Reading tolerable error
e = 0.0001

jacobiMethod(A,X,b,n)