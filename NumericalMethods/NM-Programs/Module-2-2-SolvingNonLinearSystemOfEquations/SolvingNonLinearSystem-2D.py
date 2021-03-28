import numpy as np

def printMatrix(V):
    n = len(V)
    m = len(V[0])
    for i in range(n):
        for j in range(m):
                     
            print(f'{V[i][j]:15.08f}' ,  end="  ")
            
        print()
    print()


x0 = 2
y0 = 2

e = 0.0001

f1 = lambda x,y: (x**2) + (y**2) - 9
f2 = lambda x,y: (x**2) - (y) - 9

f1x1 = lambda x,y: 2*x
f1y1 = lambda x,y: 2*y

f2x2 = lambda x,y: 2*x
f2y2 = lambda x,y: 1


i=1
condition = True
while condition:

    J = np.array([
        [f1x1(x0,y0),f1y1(x0,y0)],
        [f2x2(x0,y0),f2y2(x0,y0)]
        ])

    print("J = ")
    printMatrix(J)

    invJ = np.linalg.inv(J)
    f = np.array([[f1(x0,y0)],[f2(x0,y0)]])
    H = np.matmul(invJ,f)

    print("H = ")
    print(H)
    
    x1 = x0 - H[0][0]
    y1 = y0 - H[1][0]
   
    print(f'\nIteration = {i}   x0 = {x0:.15f}   y0 = {y0:.15f}')

    condition = (abs(x1-x0)>e and abs(y1-y0)>e)
    
    if condition == False:
        print(f"Roots found")
        print(f'Iteration = {i}   x1 = {x1:.15f}   y1 = {y1:.15f}')
        break
    
    i = i + 1
    x0 = x1
    y0 = y1
    
    