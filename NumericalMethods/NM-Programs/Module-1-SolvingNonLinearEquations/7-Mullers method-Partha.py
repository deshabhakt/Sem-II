import cmath
f= lambda x : (x**4) - 4*(x**2) - 3*x + 5
# x0=complex(-1.5,0)
x1=complex(-1.5,-1)
x2=complex(-1.5,-0.9)

count=1

x0= 1.5
# x1= -0.5
# x2= 0.0

while count<=10:
    a=(((x1-x2)*(f(x0)-f(x2)))-((x0-x2)*(f(x1)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
    b=(((x0-x2)**2*(f(x1)-f(x2)))-((x1-x2)**2*(f(x0)-f(x2))))/((x0-x2)*(x1-x2)*(x0-x1))
    c=f(x2)
    
    # # For Complex Root use this
    x3 = x2 + (-2*c)/(b-(b**2-4*a*c)**0.5)
    
    
    # For Real Roots Use this
    # x3 = x2 + (-2*c)/(max((b+(b**2-4*a*c)**0.5),(b-(b**2-4*a*c)**0.5)))
    
    print(f'count is {count}        value is {x3}')
    x0=x1
    x1=x2
    x2=x3
    count=count+1