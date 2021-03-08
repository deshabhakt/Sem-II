import numpy as np
import sys

def printMatrix(V):
    m = len(V)
    n = len(V[0])
    for i in range(m):
        for j in range(n):
            
            print(f'{V[i][j]:15.08f}' ,  end="  ")           
        print()
    print()



def luDecomposition(A,n):

    L = np.zeros((n,n))
    for i in range(n):
            L[i][i] = 1.0
    
    U = A

    for j in range(n-1):
        for i in range(j+1,n):
            if(U[j][j]==0):
                print("L = ")
                printMatrix(L)

                print("U = ")
                printMatrix(U)
                sys.exit("Zero Pivot Detected Gauss Elimination Failed")
            L[i][j] = U[i][j]/U[j][j]
            U[i,:]-=L[i][j]*U[j,:]
    return L,U


n = 3
A = np.array(((
    (3.,4.,7.),
    (6.,8.,3.),
    (1.,2.,1.)
)))

# A = np.array(((
#     (1.,2.,3.),
#     (4.,5.,6.),
#     (7.,8.,9.)
# )))

L,U = luDecomposition(A,n)

print("L = ")
printMatrix(L)

print("U = ")
printMatrix(U)