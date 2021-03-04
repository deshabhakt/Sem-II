from math import *

MaxIterations = 1000

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N=MaxIterations):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1

    while step <= N:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        
        print(f'Iteration = {step:3}, x1 = {x1:3}   f(x1) = {f(x1):3} ')
        # print(f'Iteration = {step:3}, x1 = {x1}   f(x1) = {f(x1)} ')
        
        if(abs(x1-x0)<e):
            print(f'\nRequired root is: {x1:3.06}')
            break
        x0 = x1
        step = step + 1
        
    if step > MaxIterations:
        print('\nNot Convergent.')
        
        

# Defining Function
def f(x):
    
    y = 3*cos(x-1) - x
    

    return y

# Defining derivative of function
def g(x):
    
    z = -3*sin(x-1) -1
    return z


# Input Section

x0 = 1.5
e  = 0.001

# N  = 25

# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e)