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



def luDecomposition(A,b,n):

    L = np.zeros((n,n))
    for i in range(n):
            L[i][i] = 1.0
    
    U = A
    itr=1
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
            print(f'Iteration = {itr}\n')
            itr+=1
            print("L = ")
            printMatrix(L)

            print("U = ")
            printMatrix(U)
    
    x = np.zeros(n)
    x[n-1] = b[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = b[i]
        
        for j in range(i+1,n):
            x[i] = x[i] - U[i][j]*x[j]
        
        x[i] = x[i]/U[i][i]
    print(x)
    y = np.zeros(n)
    y[n-1] = x[n-1]/L[n-1][n-1]
    for i in range(n-2,-1,-1):
        y[i] = x[i]
        
        for j in range(i+1,n):
            y[i] = y[i] - L[i][j]*y[j]
        
        y[i] = y[i]/L[i][i]
    print(y)
    return L,U


n = 4
A = np.array(((
    (1.,1.,0.,3.0),
    (2.,1.,-1.,1.0),
    (3.,-1.,-1.,2.),
    (-1.,2.,3.,-1)
)))

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

IL = np.linalg.inv(L)
print(IL)