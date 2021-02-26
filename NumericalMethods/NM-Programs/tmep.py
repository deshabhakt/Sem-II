import math
def secant(f,a,b):
    fa=f(a)
    fb=f(b)
    
    x_new=[]
    y_new=[]
    for i in range(8):
        

        c=(a*fb-b*fa)/(fb-fa)
        fc=f(c)
        x_new.append(c)
        y_new.append(fc)
        print(f'a={a.__round__(5)}  b={b.__round__(5)}  x{2+i} = {c.__round__(5)}     f(x{2+i}) = {fc.__round__(5)}')
        a=b
        fa=fb
        b=c
        fb=fc
    return c.__round__(5),x_new,y_new


x0=math.pi/2 -0.25
x1=math.pi/2

func=lambda x : math.sin(x)
sol,x,y=secant(func, x0,x1)
print(x)
print(y)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()