
# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (24-3*y)/4
f2 = lambda x,y,z: (30+z-3*x)/4
f3 = lambda x,y,z: (-24+y)/4

# Initial setup
x0 = 0
y0 = 0
z0 = 0

# Reading tolerable error
# e = float(input('Enter tolerable error: '))
e = 0.0001

# Implementation of Gauss Seidel Iteration

condition = True
count = 1

print('\n(Count, x, y, z)\n')

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    
    print('(%d, %0.20f, %0.20f, %0.20f)\n' %(count, x1,y1,z1))

    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x = %0.8f, y = %0.8f and z = %0.8f\n'% (x1,y1,z1))
