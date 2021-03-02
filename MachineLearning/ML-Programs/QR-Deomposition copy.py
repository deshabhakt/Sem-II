import numpy as np

def matrixInput():
    n = int(input("Enter Matrix size:"))
    A = np.zeros((n,n), dtype=float)
    print("Enter elements of matrix")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input())
    return (A,n)
    

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
    
    x = A[:,0].astype('float').reshape(n,1)
    addToQ(Q,Normalize(x),0)
    R[0][0]=getLength(x)
    
    for i in range(1,n):
        x = A[:,i].astype('float').reshape(n,1)
        y = A[:,i].astype('float').reshape(n,1).transpose()
        for j in range(i):
            R[j][i]=y.dot(Q[:,j].astype('float').reshape(n,1))
            x -= (R[j][i])*(Q[:,j].astype('float').reshape(n,1))
        R[i][i] = getLength(x)
        addToQ(Q,Normalize(x),i)
        
    return Q,R

def printMatrix(V):
    for i in range(n):
        for j in range(n):
            
            print(f'{V[i][j]:15.08f}' ,  end="  ")
                
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

# B = Q.__matmul__(R)
# printMatrix(B)