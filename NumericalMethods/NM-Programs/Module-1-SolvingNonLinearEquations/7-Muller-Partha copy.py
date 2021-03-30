import cmath
f= lambda x : 16*x**4 - 40*x**3 + 5*x**2 + 20*x + 6
x0 = 2.5
x1 = 2.0
x2 = 2.25
count=1
while (abs(x1-x2)>10**(-6)):
    a=(((x1-x2)*(f(x0)-f(x2)))-((x0-x2)*(f(x1)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
    b=(((x0-x2)**2*(f(x1)-f(x2)))-((x1-x2)**2*(f(x0)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
    c=f(x2)
    x3=x2 + (-2*c)/(b+(b**2-4*a*c)**0.5)
    print(f'count is {count}        x{count+2} = {x3}       a = {a}    b = {b}        c = {c}')
    x0=x1
    x1=x2
    x2=x3
    count=count+1