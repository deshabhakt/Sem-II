from math import *

# Defining Function
def f(x):
    return (exp(6*x)-(3*(log(2)**2))*exp(2*x)-(log(8))*exp(4*x)-(log(2))**3)

# Defining derivative of function
def f1(x):
    return ((6*exp(6*x))-3*((log(2))**2)*2*exp(2*x)-(log(8))*4*exp(4*x))

def f2(x):
    return ((6*6*exp(6*x))-3*((log(2))**2)*2*exp(2*x))-(log(8))*4*4*exp(4*x)
# Implementing Newton Raphson Method
def h(x):
    return f(x)/f1(x)
def g(x):
    return (((f1(x))**2)-(f(x))*f2(x))/((f1(x))**2)
def newtonRaphson(x0,e,N):
    print('\n\n*** MODIFIED NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - (h(x0)/g(x0))
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, h(x1)))
        temp=x0
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(temp-x0) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = -1
e = 0.0001
N = 250
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)