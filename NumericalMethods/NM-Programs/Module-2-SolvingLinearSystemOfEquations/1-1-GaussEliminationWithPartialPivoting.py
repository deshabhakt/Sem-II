# Importing NumPy Library
import numpy as np
import sys
import copy

# Defining Function for printing Matrix
def printMatrix(V):
       
    for i in range(n):
        for j in range(n+1):
                     
            print(f'{V[i][j]:15.08f}' ,  end="  ")
            
        print()
    print()


# Applying Gauss Elimination
def GaussElimination(a,n):
    x = np.zeros(n)
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        mx = a[i][i]
        row = -1
        for k in range(i,n):
            if(mx<a[k][i]):
                mx=a[k][i]
                row = k
        if(row!=-1):
            print("\nPerforming Partial Pivoting")
            I = np.identity(n)
            print('A = ')
            printMatrix(a)

            tmp = copy.copy(a[row,:])
            a[row,:] = copy.copy(a[i,:])
            a[i,:] = copy.copy(tmp)
            
            temp = copy.copy(I[row,:])
            I[row,:] = copy.copy(I[i,:])
            I[i,:] = copy.copy(temp)
            
            print(f"Swapping {i+1}th row with {row+1}th row\n")
            printMatrix(a)
        if(a[i][i]==0):
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
            
            print(f"Swapping {i+1}th row with {row+1}th row\n")
            print('A = ')
            printMatrix(a)

            print(f"P{j+1}{row+1} = ")
            printMatrix(I)
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            print(f'R{j+1}{i+1} = {ratio}')
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
            printMatrix(a)
    
    
    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i+1,x[i]), end = '\t')

    

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
n = 3
a = np.array([
    [4.,3.,0.,24.],
    [3.,4.,-1.,30.],
    [0.,-1.,4.,-24.]
    ])

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