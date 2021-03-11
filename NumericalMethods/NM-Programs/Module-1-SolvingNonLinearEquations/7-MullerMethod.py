from math import *
import cmath
MAX_ITERATIONS = 10000 
  
 
def Muller(x0, x1, x2, TOL, N = MAX_ITERATIONS): 
    print("\n\n*** MULLER METHOD IMPLEMENTATION ***")
    h1 = x1 - x0  
    h2 = x2 - x1 
    
    f0 = f(x0) 
    f1 = f(x1) 
    f2 = f(x2) 
    
    d1 = (f1 - f0)/h1  
    d2 = (f2 - f1)/h2 
    d = (d2-d1)/(h1+h2) 
    i = 3
    
    while i<=N: 
        
        b = d2 +h2*d
        D = ((b**2)-4*f2*d)**(1/2)
            
        if(abs(b-D) < abs(b+D)):
            E = b + D 
        else:
            E = b - D

        h = -2*f2/E
        p = x2 + h
        
        if(abs(h)<TOL):
            print(f"\n\niteration = {i:3}      x = {p:f}        f(p) = {f(p):f}") 
            break
        
        print(f'a = {d:f}                b = {b:f}              c = {f(x2):f}\n')
        print(f'\nIteration = {i:3}      p = {p:3.10f}          f(p) = {f(p):3.10f} ')
        x0 = x1
        x1 = x2
        x2 = p
        h1 = x1 - x0  
        h2 = x2 - x1 

        f0 = f(x0) 
        f1 = f(x1) 
        f2 = f(x2) 
        
        d1 = (f1 - f0)/h1  
        d2 = (f2 - f1)/h2 
        d = (d2-d1)/(h1+h2) 
    
        i += 1 
    if (i > MAX_ITERATIONS): 
        print("Root cannot be found using",  
                        "Muller's method") 

        


def f(x): 
  
    g = (x**4) - 4*(x**2) - 3*x + 5
    # g = 16*(x**4) - 40*(x**3) +5*(x**2) + 20*x + 6
    return g


# Driver Code 

# x0 = -1.5
# x1 = 2.0
# x2 = 2.1

x0 =complex(-1.5,0.0)
x1 =complex(-1.5,-1.0)
x2 =complex(-1.5,-0.9)

e = 10**(-5)

Muller(x0, x1, x2, e)
      
