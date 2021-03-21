import numpy as np
import sys

def printMatrix(V):
    m = len(V)
    n = len(V[0])
    for i in range(m):
        for j in range(n):
            
            print(f'{V[i][j]:15.06f}' ,  end="  ")           
        print()
    print()



def luDecomposition(A,b,n):

    L = np.zeros((n,n))
    for i in range(n):
            L[i][i] = 1.0
    
    U = A
    itr=1
    for j in range(n-1):
        for i in range(j+1,n):
            if(U[j][j]==0):
                sys.exit("Zero Pivot Detected Gauss Elimination Failed")
            
            L[i][j] = U[i][j]/U[j][j]
            U[i,:]-=L[i][j]*U[j,:]
            print(f'Iteration = {itr}\n')
            itr+=1
            print("L = ")
            printMatrix(L)

            print("U = ")
            printMatrix(U)
    
    return L,U


n = 4
A = np.array([
    [1., -2., -2., -3.],
    [3., -9., 0., -9.],
    [-1., 2., 4., 7.],
    [-3., -6., 26., 2.]
])

n = 3
# A = np.array(((
#     (1.,2.,3.),
#     (4.,5.,6.),
#     (7.,8.,9.)
# )))

b = np.array([8.,7.,14.,-7.])
L,U = luDecomposition(A,b,n)

print("L = ")
printMatrix(L)

print("U = ")
printMatrix(U)
