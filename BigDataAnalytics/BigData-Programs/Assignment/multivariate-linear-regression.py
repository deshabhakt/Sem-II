import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class LinearRegression:

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # gradient descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            # compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
 

    def predict(self, X):
        y_approximated = np.dot(X, self.weights) + self.bias
        return y_approximated
    
    def score(self,y,y_pred):
        return np.mean((1-abs(y-y_pred)))

    def visualize(self,x,y,y_pred):
        plt.scatter(x,y,color='r')
        plt.plot(x,y_pred,color='g')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Multivariate Linear Regression')
        plt.show()


if __name__ == '__main__':


    df = pd.DataFrame({
    'x1' : [ 1.1,  1.3,  1.5,  2. ,  2.2,  2.9,  3. ,  3.2,  3.2,  3.7,  3.9, 4. ,  4. ,  4.1,  4.5,  4.9,  5.1,  5.3,  5.9,  6. ,  6.8,  7.1, 7.9,  8.2,  8.7,  9. ,  9.5,  9.6, 10.3, 10.5],    
    'x2' : [ 2.1,  2.3,  1.4,  2.5 ,  2.9,  2.,  3. ,  3.2,  3.2,  3.7,  3.1, 4.2 ,  4.6 ,  4.3,  4.1,  4.7,  5.2,  5.4,  5.0,  6. ,  6.6,  7.1, 7.9,  8.2,  5.7,  9. ,  9.5,  9.6, 10.3, 10.5],
    'y' : [ 1.1,  1.3,  1.5,  2. ,  2.2,  2.9,  3. ,  3.2,  3.2,  3.7,  3.9, 4. ,  4. ,  4.1,  4.5,  4.9,  5.1,  5.3,  5.9,  6. ,  6.8,  7.1, 7.9,  8.2,  8.7,  9. ,  9.5,  9.6, 10.3, 10.5]
    })
    

    # Linear Regression
    le = LinearRegression()

    x = df.iloc[:,:2].values
    y = df.y.values

    le.fit(x,y)

    y_pred = le.predict(x)
    
    for i in range(len(y)):
        print(f'{y[i]}              {y_pred[i]:10.5f}')

    accuracy = le.score(y,y_pred)
    print('\nAccuracy = ',accuracy)

    # we cannot visualize resutls if number of independent variables are more than 1
    if (len(x))==1:
        le.visualize(x,y,y_pred)

    