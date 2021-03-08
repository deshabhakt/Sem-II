# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (9-2*z+y)/9
f2 = lambda x,y,z: (15-x+2*z)/10
f3 = lambda x,y,z: (17-2*y +2*x)/13

# Initial setup
x0 = 1
y0 = 1
z0 = 1

# Reading tolerable error
# e = float(input('Enter tolerable error: '))
e = 0.00001


# Implementation of Jacobi Iteration

condition = True
count = 1

print('\n(Count, x, y, z)\n')

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
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