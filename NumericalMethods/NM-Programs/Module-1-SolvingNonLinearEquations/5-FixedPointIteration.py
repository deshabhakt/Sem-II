# Fixed Point Iteration Method
# Importing math to use sqrt function
from math import *

def f(x):
    return (x**4)-3*(x**2)-3

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return (3*(x**2)+3)**(1/4)

# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        temp=x0
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(temp-x0) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
# x0 = input('Enter Guess: ')
# e = input('Tolerable Error: ')
# N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = 1
e = 0.000001

# Converting N to integer
N = 15


#Note: You can Take input from user using following commands
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
fixedPointIteration(x0,e,N)