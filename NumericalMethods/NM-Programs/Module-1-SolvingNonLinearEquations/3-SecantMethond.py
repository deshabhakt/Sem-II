from math import *

# Defining Function
def f(x):
    return cos(x) - x*exp(x)

# Implementing Secant Method

def secant(x0,x1,e,N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!') 
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print(f'Iteration-{step:3}, x2 = {x2:3.10} and f(x2) = {f(x2):3.10}')
        
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)


# Input Section
x0 = 0
x1 = 1
e = 0.001
N = 20

#Note: You can take input from user like this
# x0 = float(input('Enter First Guess: '))
# x1 = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Secant Method
secant(x0,x1,e,N)