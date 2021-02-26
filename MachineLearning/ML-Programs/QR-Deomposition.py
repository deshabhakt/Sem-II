import numpy as np

def matrixInput():
    n = int(input("Enter Matrix size:"))
    A = np.zeros((n,n), dtype=float)
    print("Enter elements of matrix")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input())
    return (A,n)
    
def makeVector(A,j):
    v = np.zeros((n,1), dtype = float)
    for i in range(n):
        v[i][0] = A[i][j]
    return v

def Normalize(v):
    sum = 0.0
    for i in v:
        sum+=i**2
    v=v/(sum**0.5)
    return v

def addToQ(Q,v,j):
    for i in range(n):
        Q[i][j] = v[i][0]

def getLength(v):
    sum = 0.0
    for i in v:
        sum+=i**2
    return sum**0.5
    
def QRDecomp(A,n):
    Q = np.zeros((n,n),dtype=float)
    R = np.zeros((n,n),dtype=float)
    
    x = makeVector(A,0)
    addToQ(Q,Normalize(x),0)
    R[0][0]=getLength(x)
    
    for i in range(1,n):
        x = makeVector(A,i)
        y = makeVector(A,i).transpose()
        for j in range(i):
            R[j][i]=y.dot(makeVector(Q,j))
            x -= (R[j][i])*(makeVector(Q,j))
        R[i][i] = getLength(x)
        addToQ(Q,Normalize(x),i)
        
    return Q,R


def printMatrix(V):
    for i in range(n):
        for j in range(n):
            if V[i][j]>=0 :
                print(f'{V[i][j]:7.05f}' ,  end="  ")
            else:
                print(f'{V[i][j]:7.04f}' ,  end="  ")
        print()
    print()

# Default Input
n = 3
A = np.array(((
    (1,2,3),
    (4,5,6),
    (7,8,9)
)))

# Uncomment following lines for custom input

# A,n = matrixInput()



Q,R = QRDecomp(A,n)

print("Q =")
printMatrix(Q)

print("R =")
printMatrix(R)

B = Q.__matmul__(R)
printMatrix(B)