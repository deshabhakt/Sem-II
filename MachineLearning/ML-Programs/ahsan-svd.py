import numpy as np

A= np.array([
    [1,2,5],
    [-1,3,1]
],dtype=float)
s= A.shape
row= s[0]
col= s[1]
m= min(row,col)
print(f"A=\n",A)
#Calculating SVD of A
M= np.matmul(A.T,A)
print(M)
evals1, evecs= np.linalg.eig(M)
evals= evals1**(0.5)
evals= evals[::-1] 
#Reversing the narray, As egin values are in ascending order
print(evals)

V= evecs

#Reversing matrix column wise as we have reversed narry of eigen values
temp= np.zeros((col,1),dtype='float')
i=0
j=col-1
while(i<j):
    temp[:,0]= V[:,i]
    V[:,i]=V[:,j]
    V[:,j]=temp[:,0]
    i+=1
    j-=1

Vt= evecs.T

D= np.zeros((row,col),dtype='float')
for i in range(m):
    D[i,i]= evals[i]

U= np.zeros((row,row),dtype='float')
for i in range(row):
    U[:,i]=np.matmul(A,V[:,i])
    U[:,i] = (1.0/evals[i])*np.matmul(A,V[:,i])

print(f"U=\n",U)
print(f"D=\n",D)
print(f"Vt=\n",Vt)
Mf= np.matmul(U,D)
Mf= np.matmul(Mf,Vt)
print(f"Mf(U*D*Vt)=\n",Mf) #Varifying my result

#The below code is for varification
print("\n")
U, D, Vt= np.linalg.svd(A)
print(f"U=\n",U)
print(f"D=\n",D)
print(f"Vt=\n",Vt)