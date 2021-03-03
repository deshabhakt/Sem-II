import cmath

MAX_ITERATIONS = 10000 
  
def f(x): 
  
    return (1 * pow(x, 3) - x + 2) 
  
def Muller(x0, x1, x2, TOL): 
  
    i = 0 
    h1 = x1 - x0  
    h2 = x2 - x1 
    
    f0 = f(x0) 
    f1 = f(x1) 
    f2 = f(x2) 
    
    d1 = (f1 - f0)/h1  
    d2 = (f2 - f1)/h2 
    d = (d2-d1)/(h1+h2) 
    i=0
    while (True): 
        i += 1 

        b = d2 +h2*d
        sq_root = ((pow(b,2))-4*f2*d)
        D = 0
        if sq_root == complex():
            D = cmath.sqrt(sq_root)
        else:
            D = (sq_root)**(1/2)
        E=0
        if(abs(b-D)<abs(b+d)):
            E = b + D
        else:
            E = b - D

        h = -2*f2/E
        p = x2 + h
        
        print(f'count is {i} -----> x: {p}')

        if(abs(h)<TOL):
            break
        
        else:
            x0=x1
            x1=x2
            x2=p
            h1 = x1 - x0  
            h2 = x2 - x1 
    
            f0 = f(x0) 
            f1 = f(x1) 
            f2 = f(x2) 
            
            d1 = (f1 - f0)/h1  
            d2 = (f2 - f1)/h2 
            d = (d2-d1)/(h1+h2) 

        if (i > MAX_ITERATIONS): 
            print("Root cannot be found using",  
                            "Muller's method") 
            break 
    if (i <= MAX_ITERATIONS): 
        print("The value of the root is", 
                          p) 
  
# Driver Code 
a = 0 
b = 1 
c = 2 
e = 0.000001
# a=complex(-0.5,1)
# b=complex(0.5,0.9)
# c=complex(0.5,0.8)
Muller(a, b, c, e)
      