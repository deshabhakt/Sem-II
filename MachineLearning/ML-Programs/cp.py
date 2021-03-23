from numpy import *
import matplotlib.pyplot as plt
import mpl_toolkits as mplot3d
#program for mixed BC

l = 20          #int(input('length of region  '))
b = 20          #int(input('breath of region  '))
c = 50           #int(input('Number of divisions on length  '))
d = 50          #int(input('Number of divisions on breath  '))


north = 1700     #int(input('value of temperature at North end  '))
west =  1725      #int(input('value of temperature at west end  '))
east =  1750     #int(input('value of temperature at east end  '))

arr = zeros([c+1, d+1]) 

for w in range(1,d):
    arr[0][w] = north

for x in range(1,c):
    arr[x][0] = west

for y in range(1,c):
    arr[y][d] = east

arr[0][0] = (north + west)/2
arr[0][d] = (north + east)/2

guess = (north + east + west)/3

for e in range(1,c):
    for f in range(1,d):
        arr[e][f] = guess

for new in range (0,d+1):
       arr[c][new] = (4*(arr[c-1][new]) - (arr[c-2][new]))/3

print(arr)

p=0 

while p <= 2 :
    
    for e in range(1,c):
        for f in range(1,d):
            arr[e][f] = ( arr[e-1][f] + arr[e+1][f] + arr[e][f-1] + arr[e][f+1] ) / 4
    
    
    for new in range (0,d+1):
       arr[c][new] = (4*(arr[c-1][new]) - (arr[c-2][new]))/3
    
    p= p+1



xmat = zeros([c+1, d+1]) 
ymat = zeros([c+1, d+1]) 

#this is for X values
for qbo in range(c+1):
        for ma in range(d+1):
            xmat[qbo][ma] = (ma)*(b/d)

#this is for Y values
for abo in range(c,-1,-1):
        for yd in range(d+1):
            ymat[abo][yd] = (c-abo)*(l/c)

#plotting

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_wireframe(xmat, ymat, arr,cmap='gnuplot_r', edgecolor='red')
# ax.plot3D(xmat.flatten(),ymat.flatten(),arr.flatten())

# ax.scatter3D(xmat, ymat, arr,s=1, c='black', marker='.') 
ax.set_title('3D line plot geeks for geeks') 
plt.show()