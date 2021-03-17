import numpy as np

def printMatrix(V):
    n = len(V)
    m = len(V[0])
    for i in range(n):
        for j in range(m):
                     
            print(f'{V[i][j]:15.08f}' ,  end="  ")
            
        print()
    print()


x0 = complex(0,-2)
y0 = complex(1,-1)
z0 = complex(5,-1)

e = 0.0001

f1 = lambda x,y,z: (x**3) + (y**3) + (z**3) - 3
f2 = lambda x,y,z: (x**3) + (y**3) + (z**3) - 13
f3 = lambda x,y,z: (x**3) + (y**3) + (z**3) + 15

f1x1 = lambda x,y,z: 3*(x**2)
f1y1 = lambda x,y,z: 3*(y**2)
f1z1 = lambda x,y,z: 3*(z**2)

f2x2 = lambda x,y,z: 3*(x**2)
f2y2 = lambda x,y,z: 3*(y**2)
f2z2 = lambda x,y,z: 3*(z**2)

f3x3 = lambda x,y,z: 3*(x**2)
f3y3 = lambda x,y,z: 3*(y**2)
f3z3 = lambda x,y,z: 3*(z**2)


i=1
condition = True
while condition:

    J = np.array([
        [f1x1(x0,y0,z0),f1y1(x0,y0,z0),f1z1(x0,y0,z0)],
        [f2x2(x0,y0,z0),f2y2(x0,y0,z0),f2z2(x0,y0,z0)],
        [f3x3(x0,y0,z0),f3y3(x0,y0,z0),f3z3(x0,y0,z0)]
        ])

    print("J = ")
    printMatrix(J)

    invJ = np.linalg.inv(J)
    f = np.array([[f1(x0,y0,z0)],[f2(x0,y0,z0)],[f3(x0,y0,z0)]])
    H = np.matmul(invJ,f)

    print("H = ")
    print(H)

    x1 = x0 - H[0][0]
    y1 = y0 - H[1][0]
    z1 = z0 - H[2][0]
   
    print(f'Iteration = {i}   x0 = {x0:.15f}   y0 = {y0:.15f}   z0 = {z0:.15f} ')

    condition = (abs(x1-x0)>e and abs(y1-y0)>e and abs(z1-z0)>e)
    
    if(condition==False):
        print(f"Roots found")
        print(f'Iteration = {i}   x1 = {x1:.15f}   y1 = {y1:.15f}   z1 = {z1:.15f}')
        break
    
    i = i + 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    