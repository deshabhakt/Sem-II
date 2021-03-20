import copy
import numpy as np

a = [1,2,3,4,5,6,7,8,9]
# b = a           # Assigns as reference

c = copy.copy(a)    # shallow copy
print('a = ',a,id(a))
print('c = ',c,id(c))

print("Shallow copy: after chaning 'a', 'c' also changes but reverse is not true")

a[8]=100
print('a = ',a)
print('c = ',c)


d = copy.deepcopy(a)
a.append(25)
print('a = ',a,id(a))
print('d = ',d,id(d))

