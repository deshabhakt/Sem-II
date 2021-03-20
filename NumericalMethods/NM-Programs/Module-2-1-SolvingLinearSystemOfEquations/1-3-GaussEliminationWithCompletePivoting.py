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
                     
            print(f'{V[i][j]:15.10f}' ,  end="  ")
            
        print()
    print()


# Applying Gauss Elimination
def GaussElimination(a,n):
    x = np.zeros(n)
    var = np.zeros(n)
    for i in range(n):
        var[i] = i+1
   
    A = copy.copy(a)

    for i in range(n):

        mx = a[i][i]
        row = -1
        column = -1
        
        for k in range(i,n):
            for l in range(i,n):
                if(mx<abs(a[k][l])):
                    mx=a[k][l]
                    row = k
                    column = l

        if(row!=-1 and column!=-1 and row!=i and column!=i):
            
            print("\nPerforming Complete Pivoting")
            print('A = ')
            printMatrix(a)

            # Swapping Columns
            I = np.identity(n)

            tmp = copy.copy(a[:,column])
            a[:,column] = copy.copy(a[:,i])
            a[:,i] = copy.copy(tmp)

            temp = copy.copy(I[:,column])
            I[:,column] = copy.copy(I[:,i])
            I[:,i] = copy.copy(temp)

            tmp = copy.copy(A[:,column])
            A[:,column] = copy.copy(A[:,i])
            A[:,i] = copy.copy(tmp)
            
            var = copy.copy(np.matmul(I,var))

            # Swapping Rows
            I2 = np.identity(n)

            tmp = copy.copy(a[row,:])
            a[row,:] = copy.copy(a[i,:])
            a[i,:] = copy.copy(tmp)
            
            temp = copy.copy(I2[row,:])
            I2[row,:] = copy.copy(I2[i,:])
            I2[i,:] = copy.copy(temp)

            print(f"Swapping Column {i+1} with column {column+1}")
            print(f"Swapping row {i+1} with row {row+1}\n")
            
            print(f"Permutation Matrices are:")
            print(f"C{i+1}{column+1} = ")
            printMatrix(I)
            
            print(f"P{i+1}{row+1} = ")
            printMatrix(I2)

            print('A = ')
            printMatrix(a)

        elif(row!=-1 and column==i):

            print("\nPerforming Complete Pivoting")
            print('A = ')
            printMatrix(a)

            # Swapping rows
            I2 = np.identity(n)

            tmp = copy.copy(a[row,:])
            a[row,:] = copy.copy(a[i,:])
            a[i,:] = copy.copy(tmp)
            
            temp = copy.copy(I2[row,:])
            I2[row,:] = copy.copy(I2[i,:])
            I2[i,:] = copy.copy(temp)

            print(f"Swapping row {i+1} with row {row+1}")
            
            print(f"Permutation Matrix is:")
            print(f"P{i+1}{row+1} = ")
            printMatrix(I2)
            
            print('A = ')
            printMatrix(a)

        elif(column!=-1 and row==i):
            
            print("\nPerforming Complete Pivoting")
            print('A = ')
            printMatrix(a)

            # Swapping Columns
            I = np.identity(n)

            tmp = copy.copy(a[:,column])
            a[:,column] = copy.copy(a[:,i])
            a[:,i] = copy.copy(tmp)

            temp = copy.copy(I[:,column])
            I[:,column] = copy.copy(I[:,i])
            I[:,i] = copy.copy(temp)
            
            tmp = copy.copy(A[:,column])
            A[:,column] = copy.copy(A[:,i])
            A[:,i] = copy.copy(tmp)

            var = copy.copy(np.matmul(I,var))

            print(f"Swapping Column {i+1} with column {column+1}")
           
            print(f"Permutation Matrix is:")
            print(f"C{i+1}{column+1} = ")
            printMatrix(I)
            
            print('A = ')
            printMatrix(a)
        
        '''
        # if pivot element is zero
        elif a[i][i]==mx==0:
            I = np.identity(n)
            print('A = ')
            printMatrix(a)
            print("\nZero Pivot Detected\n\n")
            row = 0
            for m in range(n-1,i-1,-1):
                if a[m][i]!=0:
                    row = m
                    break
            temp = copy.copy(a[row,:])
            a[row,:] = copy.copy(a[i,:])
            a[i,:] = copy.copy(temp)

            temp = copy.copy(I[row,:])
            I[row,:] = copy.copy(I[i,:])
            I[i,:] = copy.copy(temp)

            print(f"Swapping row {i+1} with row {row+1} \n")
            
            print(f"P{i+1}{row+1} = ")
            printMatrix(I)

            print('A = ')
            printMatrix(a)
        '''
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            print(f'M{j+1}{i+1} = {ratio}')
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
            print('A = ')
            printMatrix(a)
    
    
    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    # Displaying solution
    print('\nRequired solution is: \n')
    for i in range(n):
        print('X%d = %0.2f' %(var[i],x[i]), end = '\t')
    print()
    
    
    # Checking if answer is correct or not
    print('\n\n\nA = ')
    printMatrix(A)
    
    Ax = np.matmul(A[:,:-1],x)
   
    for i in range(n):
        print(f'{Ax[i]:f}\t|\t{A[i,n]:f}')


    

# Making augumented matrix
n = 4
a = np.array([
    [1., 4., -1., 1., 2.],
    [1., -2.,-3.,1.,4.],
    [4.,-1.,2.,-1.,2.],
    [0.,1.,0.,-4.,0.]
    ])

# n = 3
# a = np.array([[3.0,-2.,1.,3.],[1.,-6.,8.,2.],[2.,3.,-6.,1.]])

# n = 3
# a = np.array([
#     [4.,3.,0.,24.],
#     [3.,4.,-1.,30.],
#     [0.,-1.,4.,-24.]
#     ])

GaussElimination(a,n)


# Taking augmented matrix coefficients from user
# n = int(input('Enter number of unknowns: '))
# a = np.zeros((n,n+1))

'''
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
'''