# Importing NumPy Library
import numpy as np
import sys

# Defining Function for printing Matrix
def printMatrix(V):
       
    for i in range(n):
        for j in range(n+1):
                     
            # '''
            if j<n:
                print(f'{V[i][j]:15.08f}' ,  end="  ")
            
            else:
                print(f'| {V[i][j]:15.08f}' ,  end="  ")
            # '''
            
        print()
    print()


# Applying Gauss Elimination
def GaussElimination(a,n):
    x = np.zeros(n)
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
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

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))
# n=2

# Making augumented matrix
a = np.zeros((n,n+1))
# a = np.array([
#     [1, 4, -1, 1, 2],
#     [1, -2,-3,1,4],
#     [4,-1,2,-1,2],
#     [0,1,0,-4,0]])

# a=np.array([[1,-1,1,6],[0,1,-2,4],[1,0,-1,2]])
# a = np.array([[1,pow(10,-20),1],[1,1,2]])
a = np.array([[3,-2,1,3],[1,-6,8,2],[2,3,-6,1]])

GaussElimination(a,n)


# Taking augmented matrix coefficients from user

'''
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
'''