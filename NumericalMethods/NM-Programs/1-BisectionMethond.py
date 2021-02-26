from math import *
from matplotlib import pyplot as plt

print()
print("Bisection Method")
def f(x):
    
    # Input Function
    exp= -(x**3)-cos(x)    
    return exp

a=-1                 # First End Point
b=0                  # Second End Point
ep=0.00001           # Accuracy Required
temp = abs(b-a)
i=1
while temp>=ep:
    # print()
    plt.plot(temp,i)
    # Printing Iteration Number
    # print(f"Iteration : {i}")
    i+=1
    
    # Finding Bisection
    m=(a+b)/2
    print("b=%0.8f"%b)                    # Setting Precision using Fstring
    # print(f"m={m:0.8f}")                # Setting Precision using Fstring
    
    # Finding Function Value at a b and m
    fa=f(a)
    fm=f(m)
    fb=f(b)
    
    
    # print(f"f(a)*f(m)={fa*fm}")
    # print(f"f(b)*f(m)={fb*fm}")
    
    # Checking Interval for next iteration
    if fa*fm<0:
        b=m
        # print("a=%0.8f"%a+"  b=%0.8f"%b)             # setting precision using %
    else:
        a=m
        # print("a={0:0.8f} b={0:0.8f}".format(a,b))     # Setting Precision using .format
    # Checking Accuracy Reached
    temp = abs(b-a)
    # print(f"Accuracy Reached = {temp}")

print(f"""
    Final Solution is 'x={m:0.8f}'

        The End""")
    
plt.show()