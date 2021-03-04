import cmath
def f(x): return x**4-4*x**2-3*x+5


x0 = complex(-1.5, 0.0)
x1 = complex(-1.5, -1.0)
x2 = complex(-1.5, -0.9)
count = 1
while (abs(x1-x2) > 10**(-16)):
    a = (((x1-x2)*(f(x0)-f(x2)))-((x0-x2)*(f(x1)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
    b = (((x0-x2)**2*(f(x1)-f(x2)))-((x1-x2)**2*(f(x0)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
    c = f(x2)
    x3 = x2 + (-2*c)/(b+(b**2-4*a*c)**0.5)
    print(f'count is {count}        x{count+2} = {x3}       a= {a}    b={b}')
    x0 = x1
    x1 = x2
    x2 = x3
    count = count+1
