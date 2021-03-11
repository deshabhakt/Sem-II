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
    
    J = np.identity(n)

    L = np.zeros((n,n))
    for i in range(n):
        L[i][i] = 1.0
   
    U = copy.copy(A)
    
    itr = 0 
    for j in range(n-1):
        mx = U[j][j]
        row = -1
        column = -1
        # complete Pivoting
        for r in range(j,n):
            for s in range(j,n):
                if(U[r][s]>mx):
                    mx = U[r][s]
                    column=s
                    row=r
        
        if(row!=-1 and column!=-1 and row!=j and column!=j):
            
            print('U = ')
            printMatrix(U)
            print("\nPerforming Complete Pivoting by\n")
            
            I = copy.copy(J)

            # Swapping columns
            temp = copy.copy(U[:,column])
            U[:,column] = copy.copy(U[:,j])
            U[:,j] = copy.copy(temp)
            
            temp = copy.copy(I[:,column])
            I[:,column] = copy.copy(I[:,j])
            I[:,j] = copy.copy(temp)

            print(f"Swapping column {j+1} with column {column+1}\n")
            print('U = ')
            printMatrix(U)
            
            I2 = copy.copy(J)
            
            # Swapping rows
            temp = copy.copy(U[row,:])
            U[row,:] = copy.copy(U[j,:])
            U[j,:] = copy.copy(temp)
            
            temp = copy.copy(I2[row,:])
            I2[row,:] = copy.copy(I2[j,:])
            I2[j,:] = copy.copy(temp)
            
            print(f"Swapping row {j+1} with row {row+1}\n")
            print('U = ')
            printMatrix(U)
            
            print("\nPermutation Matrix (for Column Transformation) is: ")
            print(f"C{j+1}{column+1} = ")
            printMatrix(I)
            
            print("\nPermutation Matrix(for Row Transformation) is: ")
            print(f"P{j+1}{row+1} = ")
            printMatrix(I2)
            
        elif row==j and column!=-1:
            I = copy.copy(J)
            
            print('U =')
            printMatrix(U)
            print("\nPerforming Complete Pivoting by\n")
            
            # Swapping columns
            temp = copy.copy(U[:,column])
            U[:,column] = copy.copy(U[:,j])
            U[:,j] = copy.copy(temp)
            
            temp = copy.copy(I[:,column])
            I[:,column] = copy.copy(I[:,j])
            I[:,j] = copy.copy(temp)

            print(f"Swapping column {j+1} with column {column+1}\n")
            print('U =')
            printMatrix(U)
            
            print(f"C{j+1}{column+1} = ")
            printMatrix(I)
        elif row!=-1 and column==j:
            I = copy.copy(J)
            
            print('U =')
            printMatrix(U)
            print("\nPerforming Complete Pivoting by\n")
            
            # Swapping rows
            temp = copy.copy(U[row,:])
            U[row,:] = copy.copy(U[j,:])
            U[j,:] = copy.copy(temp)
            
            temp = copy.copy(I[row,:])
            I[row,:] = copy.copy(I[j,:])
            I[j,:] = copy.copy(temp)

            print(f"Swapping row {j+1} with row {row+1}\n")
            print('U = ')
            printMatrix(U)
            
            print(f"P{j+1}{row+1} = ")
            printMatrix(I)
        
        else:                                       # When Pivot is zero
            I = copy.copy(J)
            print('U = ')
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
            print('U = ')
            printMatrix(U)

            print(f"P{j+1}{row+1} = ")
            printMatrix(I)

        for i in range(j+1,n):               
            itr+=1
            print(f'Iteration = {itr}\n')
            
            # LU decomposition
            L[i][j] = U[i][j]/U[j][j]
            U[i,:]-=L[i][j]*U[j,:]
            
            print("L = ")
            printMatrix(L)

            print("U = ")
            printMatrix(U)

            print('='*70)

# n = 4
# A = np.array(((
#     (0.,0.,-1.,1.),
#     (1.,1.,-1.,2.),
#     (-1.,-1.,2.,0.),
#     (-1.,2.,0.,2.)
# )))

# n = 4
# A = np.array(((
#     (1.,1.,0.,3.0),
#     (2.,1.,-1.,1.0),
#     (3.,-1.,-1.,2.),
#     (-1.,2.,3.,-1)
# )))

# n = 3
# A = np.array(((
#     (1.,2.,3.),
#     (4.,5.,6.),
#     (7.,8.,9.)
# )))

# n = 3
# A = np.array(((
#     (3.,4.,7.),
#     (6.,8.,3.),
#     (1.,2.,1.)   
# )))

# n = 3
# A = np.array(((
#     (1.,2.,-1.),
#     (2.,4.,0.),
#     (0.,1.,-1.)   
# )))

n=3
n = 3
A = np.array(((
    (-2.,2.,-1.),
    (6.,-6.,7.),
    (3.,-8.,4.)
)))

b = np.array([8.,7.,14.,-7.])
luDecomposition(A,b,n)