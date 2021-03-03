
from math import *

MaxIterations = 1000

print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')

def BisectionMethod(a, b, TOL, N = MaxIterations):
    
    a = float(a)
    b = float(b)
    i = 1
    
    while i<=N:
        
        # Finding Bisection
        m = (a+b)/2
        
        # Finding Function Value at a b and m
        fa = f(a)
        fm = f(m)
        fb = f(b)
        
        print(f'iteration = {i:3}  a = {a}   b = {b}   m = {m}    f(m) = {fm}')
        
        # print(f'Iteration-{i} m = {m:3} and f(x2) = {fm:3}')
        
        if abs(fm) <=TOL or (abs(m-a)) < TOL:
            print(f'\nFinal Root Found')
            
            print(f'\niteration = {i:3}    a = {a:3.05}   b = {b:3.06}   m = {m:3.05}   f(m) = {fm:3.05}\n\n')
           
            # print(f'Iteration-{i}, m = {m:3.10} and f(x2) = {fm:3.10}')
            
            break
        i = i + 1
        
        # Checking Interval for next iteration
        if fa*fm>0:
            a = m
        else:
            b = m
    if i > N:
        print("Not Convergent")        
        

def f(x):
    
    # Input Function
    # g = (x**3) + 4*(x**2) - 10
    g = cos(x) - x*exp(x)
    g = x**3
    return g

a   = -0.5                 # First End Point
b   = 1.0               # Second End Point
TOL = 0.0001             # Accuracy Required

# N = 20


BisectionMethod(a,b,TOL)