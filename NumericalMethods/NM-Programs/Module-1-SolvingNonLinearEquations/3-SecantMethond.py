from math import *

MaxIterations = 10000

# Implementing Secant Method
def secant(x0,x1,e,N=MaxIterations):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    
    x0 = float(x0)
    x1 = float(x1)

    step = 2

    while step <= N:
        if f(x0) == f(x1):
            print('Divide by zero error!') 
            break
        
        
        x2 = x1 - (x1-x0)*f(x1)/( f(x1) - f(x0) ) 
        
        if(abs(x2-x1)<e):
            print(f'\nRequired root is: {x1:3.06}')
            break

        print(f'Iteration-{step:3}, x2 = {x2} and f(x2) = {f(x2)}')
        # print(f'Iteration = {step:3}, x1 = {x1}   Accuracy = {accuracy}   f(x1) = {f(x1)} ')
        
        x0 = x1
        x1 = x2
        step = step + 1
    
    if(step > N):
        print('\nNot Convergent.')   
        

# Defining Function
def f(x):
    return cos(x) - x*exp(x)

# Input Section
x0 = 0
x1 = 1
e = 0.0001

# N = 20

#Note: You can take input from user like this
# x0 = float(input('Enter First Guess: '))
# x1 = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Secant Method
secant(x0,x1,e)