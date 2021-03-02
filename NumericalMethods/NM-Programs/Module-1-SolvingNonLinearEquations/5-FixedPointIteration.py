# Fixed Point Iteration Method
# Importing math to use sqrt function
from mpmath import *

MaxIterations = 1000

def f(x):
    return ((x**4) - 3*(x**2) - 3)

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return (-3*pow(x,3) + pow(x,4))/3

# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N = MaxIterations):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)

        accuracy = abs(x1-x0)
        print(f'Iteration = {step:3}, x1 = {x1:3.15}   Accuracy = {accuracy:3.15}   f(x1) = {f(x1):3.15} ')
                
        if step > MaxIterations or step > N:
            flag=0
            break

        condition = accuracy > e
        
        x0=x1
        step = step + 1
        
    if flag==1:
        print(f'\nRequired root is: {x1:3.15}')
    else:
        print('\nNot Convergent.')


# Converting x0 and e to float
x0 = 1
e = 0.01

#Note: You can Take input from user using following commands
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
fixedPointIteration(x0,e)