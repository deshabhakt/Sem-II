import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class PolynomialRegression:
    def __init__(self, learning_rate=0.001, n_iters=1000,degree=2):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.coefficients = None
        self.degree = degree

    def fit(self, x, y):

        X_t = []
        y_t = []
        n = len(x)

        X_t.append(n)
        i = 1
        while(True):
            X_t.append(sum((x**i)))
            if(i/2 == self.degree):
                break
            i += 1   
        
        y_t.append(sum(y))
        for i in range(1,self.degree+1):        
            y_t.append(sum((x**i)*y))
        
        A = np.zeros((self.degree+1,self.degree+1),dtype=float)
        b = np.zeros((self.degree+1,1),dtype=float)

        for i in range(self.degree+1):
            k = i
            for j in range(self.degree+1):
                A[i,j] = X_t[k]
                k +=1
        
        for i in range(self.degree+1):
            b[i,0] = y_t[i]

        self.coefficients = np.matmul(np.linalg.inv(A),b)
 

    def predict(self, X):
        y_approximated = np.zeros(len(X))
        for i in range(0,self.degree+1):
            for j in range(len(X)):
                y_approximated[j] += self.coefficients[i]*(X[j]**i)
        return y_approximated
    
    def score(self,y,y_pred):
        accuracy = 0
        for i in range(len(y)):
             accuracy += abs(1-(y[i][0]-y_pred[i]))
        return accuracy/len(y)
    
    def visualize(self,x,y,y_pred):
        plt.scatter(x,y,color='r')
        plt.plot(x,y_pred,color='g')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Polynomial Regression')
        plt.show()


if __name__ == '__main__':

    # Polynomial Regression 

    df = pd.DataFrame({
        'x' : [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149],
        
        'y' : [5, 140, 455, 950, 1625, 2480, 3515, 4730, 6125, 7700, 9455, 11390, 13505, 15800, 18275, 20930, 23765, 26780, 29975, 33350, 36905, 40640, 44555, 48650, 52925, 57380, 62015, 66830, 71825, 77000, 82355, 87890, 93605, 99500, 105575, 111830, 118265, 124880, 131675, 138650, 145805, 153140, 160655, 168350, 176225, 184280, 192515, 200930, 209525, 218300]
    })

    le = PolynomialRegression()

    x = df.x.values
    x = x.reshape(len(x),1)
    y = df.y.values
    y = y.reshape(len(y),1)

    le.fit(x,y)

    y_pred = le.predict(x)
    for i in range(len(y)):
        print(f'\t{y[i][0]}              {y_pred[i]:10.5f}')

    accuracy = le.score(y,y_pred)
    print('Accuracy = ',accuracy)

    le.visualize(x,y,y_pred)
