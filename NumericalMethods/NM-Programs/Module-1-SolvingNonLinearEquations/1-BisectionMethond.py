import numpy as np
import math

MaxIterations = 1000
print()
print("Bisection Method")

def BisectionMethod(f,a,b,TOL):
    i=1
    while i<=MaxIterations:
        
        # Finding Bisection
        m=(a+b)/2
        
        # Finding Function Value at a b and m
        fa=f(a)
        fm=f(m)
        fb=f(b)
        accuracy = (b-a)/2
        
        if fm==0 or (accuracy<TOL):
            print(f'\nFinal Root Found')
            print(f'\niteration = {i:3} ---->  x = {m:10.10} -----> accuracy = {accuracy:4.10} -----> f(m) = {fm:10.10}\n\n')
            break
        
        # Checking Interval for next iteration
        if fa*fm>0:
            a=m
        else:
            b=m
            
        print(f'iteration = {i:3}        x = {m:15.10}      accuracy = {accuracy:4.20}       f(m) = {fm:.10}')
        i=i+1

def f(x):
    
    # Input Function
    g= x**2 - 4*x + 4 - math.log(x)  

    return g

a   = 1                 # First End Point
b   = 2                  # Second End Point
TOL = pow(10,-5)           # Accuracy Required

BisectionMethod(f,a,b,TOL)