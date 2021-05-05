import sympy as sp
import math
x=sp.Symbol('x')
f=sp.cos(x)-x*(sp.exp(x))
df=sp.diff(f)
print(df)


def newton_raphson(f,df,a):
    fa=f(a)
    dfa=df(a)
    print (f'x0 = {a.__round__(6)}      f(x0)={f(a).__round__(6)}')
    i=0
    while (abs(fa)>10**(-6)):
        c=a-(fa/dfa)
        print (f'x{i+1} = {c.__round__(6)}      f(x{i+1})={f(c).__round__(6)}')
        fc=f(c)
        a=c
        fa=fc
        dfa=df(c)
        i=i+1
    return c

# func=lambda x : (x*sp.sin(x)+sp.cos(x))
# dfunc= lambda x : x*sp.cos(x)
# z=newton_raphson(func,dfunc,3.1416)


# func= lambda x : 2*x**2 - x**3 -2
# dfunc= lambda x : 4*x - 3*x**2
# sol=newton_raphson(func,dfunc,1)

# func= lambda x : sp.cos(x)-x*(sp.exp(x))
# dfunc = lambda x : -x*sp.exp(x) - sp.exp(x) - sp.sin(x)
# sol=newton_raphson(func,dfunc,0.75)


# func= lambda x : -x**(3)-math.cos(x)
# dfunc= lambda x : -3*x**2 + math.sin(x) 
# sol=newton_raphson(func,dfunc,-0.75)


func= lambda x: x- 4*math.sin(x)
dfunc= lambda x: 1-4*math.cos(x)
sol=newton_raphson(func,dfunc,1)