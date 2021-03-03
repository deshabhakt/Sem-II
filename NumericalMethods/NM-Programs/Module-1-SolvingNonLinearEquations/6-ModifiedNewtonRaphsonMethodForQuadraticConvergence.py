from math import *

MaxIterations = 1000

# Implementing Newton Raphson Method
def h(x):
    return f(x)/f1(x)
def g(x):
    return (((f1(x))**2)-(f(x))*f2(x))/((f1(x))**2)

def modifiedNewtonRaphson(x0,e,N=MaxIterations):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1

    while step <= N:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - h(x0)/g(x0)
        
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
    return (x**3) + 4*(x**2) -10

# Defining derivative of function
def f1(x):
    return 3*(x**2) + 4*2*x

def f2(x):
    return 3*2*x + 8


# Input Section

x0 = 1.5
e  = 0.001
N  = 25

# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
modifiedNewtonRaphson(x0,e,N)