import numpy as np
import copy


def printMatrix(V):
    m = len(V)
    n = len(V[0])
    for i in range(m):
        for j in range(n):
            
            print(f'{V[i][j]:15.08f}',  end="  ")
        
        print()
    print()


def luDecomposition(A, n):

    P = []           # To Store Permutation Matrices

    U = copy.copy(A)

    tmpL = np.identity(n)

    itr = 0
    for j in range(n-1):
        mx = U[j][j]
        row = -1
        # Partial Pivoting
        for m in range(j+1, n):
            if(abs(U[m][j]) > mx):
                mx = U[m][j]
                row = m
        if(row != -1):
            I = np.identity(n)

            print('U = \n')
            printMatrix(U)
            print("\nPerforming Partial Pivoting by\n")

            # Swapping rows
            temp = copy.copy(U[row, :])
            U[row, :] = copy.copy(U[j, :])
            U[j, :] = copy.copy(temp)

            temp = copy.copy(I[row, :])
            I[row, :] = copy.copy(I[j, :])
            I[j, :] = copy.copy(temp)

            P.append(I)
            tmpL = np.matmul(I, tmpL)

            print(f"Swapping row {j+1} with row {row+1}\n")
            print('U = \n')
            printMatrix(U)

            print(f"P{j+1}{row+1} = ")
            printMatrix(I)

        for i in range(j+1, n):
            itr += 1
            print(f'Iteration = {itr}\n')

            I = np.identity(n)

            # LU decomposition
            ratio = U[i][j]/U[j][j]
            U[i, :] -= ratio*U[j, :]
            I[i][j] = -ratio

            tmpL = np.matmul(I, tmpL)

            print("U = ")
            printMatrix(U)
            print('='*70)

    ActualL = np.linalg.inv(tmpL)           # Calculating L

    p = np.identity(n)          # Variable to hold Final Permutation Matrix

    for i in range(len(P)):
        ActualL = copy.copy(np.matmul(P[i], ActualL))
        p = np.matmul(P[i],p)
    
    
    k = np.identity(n)      # Variable to hold transpose of final permutation matrix
    for i in P:
        k = np.matmul(i,k)
    
    print("P = ")
    printMatrix(p)

    print("L = ")
    printMatrix(ActualL)

    print("U = ")
    printMatrix(U)

    print("Modified Input Matrix = ")
    printMatrix(np.matmul(ActualL, U))

    print("Original Input Matrix = ")
    printMatrix(A)

    print("(inv(P))*L*U = ")
    printMatrix(np.matmul(k.transpose(),np.matmul(ActualL,U)))



# Input Section

n = 4

# A = np.array([
#     [1., -2., -2., -3.],
#     [3., -9., 0., -9.],
#     [-1., 2., 4., 7.],
#     [-3., -6., 26., 2.]
# ])

A = np.array([
    [2.,1.,1.,0.],
    [4.,3.,3.,1.],
    [8.,7.,9.,5.],
    [6.,7.,9.,8.]
])

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
#     (-1.,2.,3.,-1.)
# )))

# n = 3
# A = np.array(((
#     (-2.,2.,-1.),
#     (6.,-6.,7.),
#     (3.,-8.,4.)
# )))

# A = np.array(((
#     (1.,2.,3.),
#     (4.,5.,6.),
#     (7.,8.,9.)
# )))

# A = np.array(((
#     (3.,4.,7.),
#     (6.,8.,3.),
#     (1.,2.,1.)
# )))


luDecomposition(A, n)
