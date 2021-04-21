# Power Method to Find Largest Eigen Value and Eigen Vector
# Importing NumPy Library
import numpy as np
import sys
import copy

'''
def customInput():
    # Reading order of matrix
    n = int(input('Enter order of matrix: '))

    # Making numpy array of n x n size and initializing
    # to zero for storing matrix
    a = np.zeros((n, n))

    # Reading matrix
    print('Enter Matrix Coefficients:')
    for i in range(n):
        for j in range(n):
            a[i][j] = float(input('a['+str(i)+'][' + str(j)+']='))

    # Making numpy array n x 1 size and initializing to zero
    # for storing initial guess vector
    x = np.zeros((n))

    # Reading initial guess vector
    print('Enter initial guess vector: ')
    for i in range(n):
        x[i] = float(input('x['+str(i)+']='))

    # Reading tolerable error
    tolerable_error = float(input('Enter tolerable error: '))

    # Reading maximum number of steps
    max_iteration = int(input('Enter maximum number of steps: '))
    return a,x,tolerable_error,max_iteration
'''

# Power Method Implementation
def powerMethod(a, x, tolerable_error, max_iteration=100):

    n = len(a)    
    lambda_old = 1.0
    condition = True
    step = 1
    while condition:
        # Multiplying a and x
        # ax = copy.copy(x)
        x = np.matmul(a, x)
        Ax = copy.copy(x)
        
        # t = (Ax.dot(ax))/(ax.dot(ax))

        # Finding new Eigen value and Eigen vector
        lambda_new = max(abs(x))

        x = x/lambda_new
        
        rel_error = abs(lambda_old-lambda_new)/abs(lambda_new)

        # Displaying Eigen value and Eigen Vector
        print('\nSTEP %d' % (step))
        # print('----------')
        # print(f'Eigen Value = {lambda_new:0.4f}')
        # print(Ax,"\n")
        # print('Eigen Vector: ')
        # for i in range(n):
        #     print(f'{x[i]:0.3f}\t')
        print(f"lambda old = {lambda_old}\nlambda new = {lambda_new}")
        print("\nRelativeError = ", rel_error,"\n")


        # Checking maximum iteration
        step = step + 1
        if step > max_iteration:
            print('Not convergent in given maximum iteration!')
            break

        # Calculating error
        error = abs(lambda_new - lambda_old)
        print('errror=' + str(error))
        lambda_old = lambda_new
        condition = error > tolerable_error


# Input Matrix
A = np.array([
    [3,3,0],
    [3,5,0],
    [0,0,6]
])

# A = np.array([
#     [1,5],
#     [5,6]
# ])

# Initial Guess vector
x = np.array([1,1,1])

# error
e = 0.0001

eigVals, eigVecs = np.linalg.eig(A)
print(eigVals)
powerMethod(A,x,e,10)
