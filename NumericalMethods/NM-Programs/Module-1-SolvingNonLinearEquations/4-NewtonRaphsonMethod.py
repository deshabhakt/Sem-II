from math import *

MaxIterations = 1000

# Defining Function
def f(x):
    return cos(x) - x

# Defining derivative of function
def g(x):
    return -sin(x) - x


# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N=MaxIterations):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = -1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        
        accuracy = abs(x1-x0)

        print(f'Iteration = {step:3}, x1 = {x1:3.15}   Accuracy = {accuracy:3.15}   f(x1) = {f(x1):3.15} ')
        
        if(f(x1)==0 or accuracy < e):
            condition = False
        
        x0 = x1
        step = step + 1
        
        if step > N or step > MaxIterations:
            flag = 0
            break
        else:
            flag = 1
            
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = pi/2
e = 0.0001
N = 200
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e)