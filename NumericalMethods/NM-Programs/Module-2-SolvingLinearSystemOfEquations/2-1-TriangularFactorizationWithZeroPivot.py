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
    
    J = np.identity(n)

    itr = 0 
    for j in range(n-1):
        for i in range(j+1,n):
            
            if( U[j][j]==0):
                I = copy.copy(J)
                print('U = \n')
                printMatrix(U)
                print("\nZero Pivot Detected Gauss Elimination Failed\n\n")
                row = 0
                for m in range(n-1,j-1,-1):
                    if U[m][j]!=0:
                        row = m
                        break
                temp = copy.copy(U[row,:])
                U[row,:] = copy.copy(U[j,:])
                U[j,:] = copy.copy(temp)

                temp = copy.copy(I[row,:])
                I[row,:] = copy.copy(I[j,:])
                I[j,:] = copy.copy(temp)

                print(f"Swapping {j+1}th row with {row+1}th row\n")
                print('U = \n')
                printMatrix(U)

                print(f"P{j+1}{row+1} = ")
                printMatrix(I)
                
            itr+=1
            print(f'Iteration = {itr}\n')
            L[i][j] = U[i][j]/U[j][j]
            U[i,:]-=L[i][j]*U[j,:]
            print("L = ")
            printMatrix(L)

            print("U = ")
            printMatrix(U)
            


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