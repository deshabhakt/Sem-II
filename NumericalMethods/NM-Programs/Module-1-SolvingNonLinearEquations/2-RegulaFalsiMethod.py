# Regula Falsi method is same as secant method but secant method does not insure bracketing where as Regula Falsi does

from math import *

# Implementing False Position Method
def falsePosition(x0,x1,e,N):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition :
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print(f'Iteration-{step}, x2 = {x2:3.10} and f(x2) = {f(x2):3.10}')
        # print(f"{abs(x1-x0)}")
       
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        
        condition = abs(f(x2)) > e
        
        if step > N:
            print('Not Convergent!')
            break
        

    print('\nRequired root is: %0.8f' % x2)

# Defining Function
def f(x):
    return cos(x) - x*exp(x)

# Input Section
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Number of Steps: '))
x0 = 0
x1 = 1
e  = 0.001
N  = 20

# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e,N)