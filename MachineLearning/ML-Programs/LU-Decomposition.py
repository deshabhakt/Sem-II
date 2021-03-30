import numpy as np
import copy 

# print("Enter the size of matrix: ")
# n= int(input())

# A= np.zeros((n,n),dtype=float)
# print("Now enter elements of matrix 'A':")
# for i in range(n):
#     print("Enter elements for row:",i+1)
#     for j in range(n):
#         A[i][j]=int(input())


def printMatrix(V):
    for i in range(n):
        for j in range(n):
            
            print(f'{V[i][j]:15.08f}' ,  end="  ")
        print()
    print()


def LUDecomposition(A,n):
    L= np.zeros((n,n),dtype=float)
    for i in range(len(L)):
        L[i][i]=1

    U = copy.copy(A)    # copying matrix A into U

    for i in range(0,n-1):
        for j in range(i+1,n):
            L[j][i]= (U[j][i]/U[i][i])
            U[j][:]=U[j][:]-L[j][i]*U[i][:]

    return L,U

n = 3
A = np.array(((
    (1,2,3),
    (4,5,6),
    (7,8,9)
)))

L,U = LUDecomposition(A,n)
print("L = ")
printMatrix(L)

print("U = ")
printMatrix(U)
