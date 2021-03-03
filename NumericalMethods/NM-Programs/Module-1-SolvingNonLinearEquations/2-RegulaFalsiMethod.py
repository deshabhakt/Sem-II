# Regula Falsi method is same as secant method but secant method does not insure bracketing where as Regula Falsi does

from math import *
MaxIterations = 10000


# Implementing False Position Method
def falsePosition(x0 ,x1 ,e ,N=MaxIterations):

    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')

    step = 2
    
    while step <= N :
        
        # x2 = (x0*f(x1) - x1*f(x0))/( f(x1) - f(x0) )      # Both formula's are same 
        x2 = x1 - (f(x1)*(x1-x0))/(f(x1) - f(x0))
        

        print(f'Iteration-{step:3}, x2 = {x2} and f(x2) = {f(x2)}')
        # print(f'Iteration = {step:3}, x1 = {x1}   Accuracy = {accuracy}   f(x1) = {f(x1)} ')

        if(abs(x2-x1)<e or f(x2) <e):
            print(f'\nRequired root is: {x2:3.06}')
            break

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
                
    if step > N:
        print('Not Convergent!')

# Defining Function
def f(x):
    
    g = cos(x) - x*exp(x)
    
    return g

# Input Section

x0 = 0.0
x1 = 1.0
e  = 0.0001

# N = 20

# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Number of Steps: '))


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)
