import numpy as np

def matrixInput():
    m = int(input("Enter row size :"))
    n = int(input("Enter column size :"))

    A = np.zeros((m,n), dtype=float)
    
    print("Enter elements of matrix: ")
    for i in range(m):
        for j in range(n):
            A[i][j] = float(input())
    
    return (A,n)


def Normalize(v):
    sum = 0.0
    for i in v:
        sum+=i**2
    v=v/(sum**0.5)
    return v

def QRDecomp(A):
    
    n = len(A[0])   # Columns/Vectors
    m = len(A)      # Rows/Components
    q = []
    
    q.append(Normalize(A[:,0].reshape(m,1)))
    
    for i in range(1,n):
        
        vec = A[:,i].astype('float64').reshape(m,1)
        temp = np.zeros((m,1),dtype=float)

        for j in range(i):

            multiplier = (((vec.transpose()).dot((q[j]))))/(q[j].transpose().dot(q[j]))
            temp -= (multiplier)*q[j]
        
        vec = vec + temp
        normalizedvec = Normalize(vec)
        q.append(normalizedvec)
    
    Q = np.array(q).transpose().reshape(m,n)            # typecasting python list to numpy array and taking np.array's transpose
    
    # Calculating R
    R = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i<=j:
                R[i][j] = A[:,j].transpose().dot(Q[:,i])

    return Q,R


def printMatrix(V):
    m = len(V)
    n = len(V[0])
    for i in range(m):
        for j in range(n):
                print(f'{V[i][j]:10.05f}' ,  end="  ")
        print()
    print()

# Default Input

A = np.array(((
    (1, -1, 4),
    (1, 4, -2),
    (1, 4, 2),
    (1, -1, 0)
)))

# A = np.array([
#     [1,2,4],
#     [0,0,5],
#     [0,3,6]
# ])

Q,R = QRDecomp(A)

print("Q =")
printMatrix(Q)

print("R =")
printMatrix(R)

# Uncomment following lines for custom input

# A,n = matrixInput()
