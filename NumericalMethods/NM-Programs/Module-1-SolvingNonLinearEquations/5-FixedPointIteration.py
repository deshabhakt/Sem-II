# Fixed Point Iteration Method
# Importing math to use sqrt function
from math import *

MaxIterations = 1000

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
        
        # print(f'Iteration = {step:3}, x1 = {x1}   Accuracy = {accuracy}   f(x1) = {f(x1)} ')
                
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

def f(x):
    return cos(x) - x*exp(x)

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return (cos(x)/exp(x))

# Converting x0 and e to float
x0 = 0
e = 0.001

#Note: You can Take input from user using following commands
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
fixedPointIteration(x0,e)