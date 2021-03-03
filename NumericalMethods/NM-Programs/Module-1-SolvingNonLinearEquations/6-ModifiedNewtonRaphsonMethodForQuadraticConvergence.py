from math import *

# Implementing Newton Raphson Method
def h(x):
    return f(x)/f1(x)
def g(x):
    return (((f1(x))**2)-(f(x))*f2(x))/((f1(x))**2)
def modifiedNewtonRaphson(x0,e,N):
    print('\n\n*** MODIFIED NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - (h(x0)/g(x0))
        print(f'Iteration-{step:3}, x1 = {x1:3.08} and f(x1) = {h(x1):3.08}')
        temp = x0
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(h(x0)) > e
    
    if flag==1:
        print(f'\nRequired root is: {x1:3.08}')
    else:
        print('\nNot Convergent.')

# Defining Function
def f(x):
    return cos(x) - x*exp(x)

# Defining derivative of function
def f1(x):
    return -sin(x) - x*exp(x) - exp(x)

def f2(x):
    return -cos(x) - x*exp(x) - exp(x) - exp(x)


# Input Section
x0 = 0
e = 0.001
N = 25
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
modifiedNewtonRaphson(x0,e,N)