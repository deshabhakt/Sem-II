import numpy as np
import sys
import copy

def printMatrix(V):
    m = len(V)
    n = len(V[0])
    for i in range(m):
        for j in range(n):
            print(f'{V[i][j]:15.08f}' ,  end="  ")           
        print()
    print()

 
def luDecomposition(A,b,n):
    L = np.zeros((n,n))
    for i in range(n):
        L[i][i] = 1.0
    U = copy.copy(A)
    itr = 0 
    for j in range(n-1):
        for i in range(j+1,n):
            
            if( U[j][j]==0):
                print('A = \n')
                printMatrix(A)
                print("\nZero Pivot Detected Gauss Elimination Failed\n\n")
                row = 0
                for m in range(n-1,j-1,-1):
                    if U[m][j]!=0:
                        row = m
                        break
                temp = copy.copy(A[row,:])
                A[row,:] = copy.copy(A[j,:])
                A[j,:] = copy.copy(temp)
                temp = copy.copy(U[row,:])
                U[row,:] = copy.copy(U[j,:])
                U[j,:] = copy.copy(temp)
                print(f"Swapping {j+1}th row with {m+1}th row\n")
                print('A = \n')
                printMatrix(A)
            itr+=1
            print(f'Iteration = {itr}\n')
            L[i][j] = U[i][j]/U[j][j]
            U[i,:]-=L[i][j]*U[j,:]
            print("L = ")
            printMatrix(L)

            print("U = ")
            printMatrix(U)
            
    
    # x = np.zeros(n)
    # x[n-1] = b[n-1]/U[n-1][n-1]
    # for i in range(n-2,-1,-1):
    #     x[i] = b[i]
        
    #     for j in range(i+1,n):
    #         x[i] = x[i] - U[i][j]*x[j]
        
    #     x[i] = x[i]/U[i][i]


n = 3
# A = np.array(((
#     (0.,0.,-1.,1.),
#     (1.,1.,-1.,2.),
#     (-1.,-1.,2.,0.),
#     (-1.,2.,0.,2.)
# )))

# A = np.array(((
#     (1.,1.,0.,3.0),
#     (2.,1.,-1.,1.0),
#     (3.,-1.,-1.,2.),
#     (-1.,2.,3.,-1)
# )))

# A = np.array(((
#     (1.,2.,3.),
#     (4.,5.,6.),
#     (7.,8.,9.)
# )))

A = np.array(((
    (3.,4.,7.),
    (6.,8.,3.),
    (1.,2.,1.)   
)))

L = np.zeros((n,n))
for i in range(n):
        L[i][i] = 1.0
b = np.array([8.,7.,14.,-7.])
luDecomposition(A,b,n)

# IL = np.linalg.inv(L)
# print(IL)