#!/usr/bin/env python
# coding: utf-8

# # Lagrangian

# In[95]:


import numpy as np
import math as mt
import sympy as sp

X=sp.Symbol('X')

x=np.array([1,2,7,8])
y=np.array([4,5,5,4])
Y=0
L=1

n=x.size
i=0
j=0
for i in range (n):
    for j in range (n):
        if(j!=i):
            L=L*(X-x[j])/(x[i]-x[j])
    L=L*y[i]
    Y=Y+L
    L=1
#print(Y)
Y=sp.simplify(Y)
e=Y.subs(X,4.5)    
print('polynomial eqn:\n',Y,'\n\nEvaluated value of the polynomial:\n',e)       


# # Max Error

# In[103]:


X=sp.Symbol('X')

x=np.array([2,2.75,4])
df=sp.diff(sp.sin(x),X)

a = 0
b = 1
n=x.size
y=1

for i in range (n):
    y=y*(X-x[i])

for i in range (n-1):
    df=sp.diff(df,X)

fact=1
for i in range (1,n+1):
    fact=fact*i
Y = sp.expand(y)
e=abs(df.subs(X,a)*Y.subs(X,b)/fact)

print('function after n diff:\n',df,'\n\noriginal polynomial:\n',y,'\n\nexpanded polynomial:\n',Y,'\n\n max error:\n',e) 
print(fact)


# In[ ]:





# In[ ]:




