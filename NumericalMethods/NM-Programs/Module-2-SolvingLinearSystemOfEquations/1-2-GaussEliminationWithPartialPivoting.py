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
                     
            # '''
            if j<n:
                print(f'{V[i][j]:15.08f}' ,  end="  ")
            
            else:
                print(f'| {V[i][j]:15.08f}' ,  end="  ")
            # '''
            
        print()
    print()


# Applying Gauss Elimination
def GaussElimination(A,n):
    x = np.zeros(n)  

    U = copy.copy(A)

    P = np.identity(n)
    
    itr = 0 
    for j in range(n):
        mx = U[j][j]
        row = -1
        # Partial Pivoting
        for m in range(j+1,n):
            if(U[m][j]>mx):
                mx = U[m][j]
                row = m
        if(row!=-1):
            I = np.identity(n)
            
            print('U = \n')
            printMatrix(U)
            print("\nPerforming Complete Pivoting by\n")
            
            # Swapping rows
            temp = copy.copy(U[row,:])
            U[row,:] = copy.copy(U[j,:])
            U[j,:] = copy.copy(temp)
            
            temp = copy.copy(I[row,:])
            I[row,:] = copy.copy(I[j,:])
            I[j,:] = copy.copy(temp)

            P = np.matmul(I,P)

            print(f"Swapping row {j+1} with row {row+1}\n")
            print('U = \n')
            printMatrix(U)
            
            print(f"P{j+1}{row+1} = ")
            printMatrix(I)

        if( U[j][j]==0):
                I = np.identity(n)
                print('U = \n')
                printMatrix(U)
                print("\nZero Pivot Detected Gauss Elimination Failed\n\n")
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
            
                P = np.matmul(I,P)

                print(f"Swapping {j+1}th row with {row+1}th row\n")
                print('U = \n')
                printMatrix(U)

                print(f"P{j+1}{row+1} = ")
                printMatrix(I)
                    
        for i in range(j+1,n):               
            itr+=1
            print(f'Iteration = {itr}\n')
            
            # LU decomposition
            U[i,:]-=(U[i][j]/U[j][j])*U[j,:]

            print("U = ")
            printMatrix(U)

    # Back Substitution
    
    x[n-1] = A[n-1][n]/A[n-1][n-1]
    print(x[n-1])
    for i in range(n-2,-1,-1):
        x[i] = A[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
        
        x[i] = x[i]/A[i][i]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i+1,x[i]), end = '\t')

    print("\n\nOriginal Matrix A = ")
    printMatrix(A)
    chk = np.matmul(A[:,:-1],x)
    print()
    for i in range(n):
        print(f'{chk[i]:f}\t|\t{A[i,-1]:f}')


# Making augumented matrix
# A = np.array([
#     [1, 4, -1, 1, 2],
#     [1, -2,-3,1,4],
#     [4,-1,2,-1,2],
#     [0,1,0,-4,0]])
n = 3
A=np.array([[1.,-1.,1.,6.],[0.,1.,-2.,4.],[1.,0.,-1.,2.]])
# A = np.array([[1,pow(10,-20),1],[1,1,2]])
A = np.array([[3.0,-2.,1.,3.],[1.,-6.,8.,2.],[2.,3.,-6.,1.]])

GaussElimination(A,n)


# Taking augmented matrix coefficients from user
# n = int(input('Enter number of unknowns: '))

# A = np.zeros((n,n+1))

'''
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        A[i][j] = float(input( 'A['+str(i)+']['+ str(j)+']='))
'''