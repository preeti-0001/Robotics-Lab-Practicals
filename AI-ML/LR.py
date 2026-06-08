import numpy as np
import random
import matplotlib.pyplot as plt

def generate_dataset(number = 50, m=10, c=10):
    np.random.seed(number)
    x = np.linspace(0, 20, number)
    y = m * x + c + np.random.normal(0, number, number)
    return x,y

def linear_fit(x,y):
    x_mean, y_mean = np.mean(x), np.mean(y)
    m = np.sum((x_mean - x)*(y_mean - y))/np.sum((x-x_mean)**2)
    c= y_mean - m * x_mean
    return m,c

def plot(x,y,m,c):
    plt.scatter(x,y,color="blue", label="Data Point")
    y_pred=m*x + c
    plt.plot(x, y_pred, color="red", label="Predicted Line")
    plt.xlabel('Independent Variable (x)')
    plt.ylabel('Dependent Variable (y)')
    plt.title('Simple Linear Regression Fit')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    x, y = generate_dataset(50,10,10)

    m,c = linear_fit(x,y)

    plot(x,y,m,c)




if __name__ == "__main__":
    main()
