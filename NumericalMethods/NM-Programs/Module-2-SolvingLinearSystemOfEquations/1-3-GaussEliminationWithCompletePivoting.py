# Importing NumPy Library
import numpy as np
import sys
import copy

# Defining Function for printing Matrix
def printMatrix(V):

    m = len(V)
    n = len(V[0])   
    for i in range(m):
        for j in range(n):
                     
            print(f'{V[i][j]:15.08f}' ,  end="  ")
            
        print()
    print()


# Applying Gauss Elimination
def GaussElimination(A,n):
    x = np.zeros(n)  
    
    O_A = copy.copy(A)

    var = np.zeros(n)
    for i in range(1,n+1):
        var[i-1] = i

    U = copy.copy(A)
    
    J = np.identity(n)
    
    itr = 0 
    
    for j in range(n):
        
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

            temp = copy.copy(A[:,column])
            A[:,column] = copy.copy(A[:,j])
            A[:,j] = copy.copy(temp)
            
            # A = np.matmul(I,A)

            temp = copy.copy(var[column])
            var[column] = copy.copy(var[j])
            var[j] = copy.copy(temp)

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

            temp = copy.copy(var[column])
            var[column] = copy.copy(var[j])
            var[j] = copy.copy(temp)

            temp = copy.copy(A[:,column])
            A[:,column] = copy.copy(A[:,j])
            A[:,j] = copy.copy(temp)

            # A = np.matmul(I,A)

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
            print("\nZero Pivot Detected\n\n")
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
            
            factor = (U[i][j]/U[j][j])
            U[i,:]-=factor*U[j,:]
            
            print("U = ")
            printMatrix(U)
    
    
    # Back Substitution
    x[n-1] = O_A[n-1][n]/O_A[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = O_A[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - O_A[i][j]*x[j]
        
        x[i] = x[i]/O_A[i][i]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %f' %(var[i],x[i]) , end = '\t')
    
    
    print()
    print("Input Matrix ")
    printMatrix(O_A)
    print("Updated")
    printMatrix(A)
    CheckMatrix = np.matmul(O_A[:,:-1],x)

    for i in range(n):
        print(f'{CheckMatrix[i]:f}\t{O_A[i,-1]:f}')



# Reading number of unknowns
# n = int(input('Enter number of unknowns: '))
# n=2

# Making augumented matrix
# O_A = np.zeros((n,n+1))
# O_A = np.array([
#     [1, 4, -1, 1, 2],
#     [1, -2,-3,1,4],
#     [4,-1,2,-1,2],
#     [0,1,0,-4,0]])

O_A=np.array([[1.,-1.,1.,6.],[0.,1.,-2.,4.],[1.,0.,-1.,2.]])
# O_A = np.array([[1,pow(10,-20),1],[1,1,2]])
# O_A = np.array([[3.0,-2.,1.,3.],[1.,-6.,8.,2.],[2.,3.,-6.,1.]])
n=3
GaussElimination(O_A,n)


# Taking augmented matrix coefficients from user

'''
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        O_A[i][j] = float(input( 'O_A['+str(i)+']['+ str(j)+']='))
'''