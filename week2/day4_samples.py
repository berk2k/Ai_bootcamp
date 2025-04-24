import sympy as sp

x = sp.Symbol('x')
f = x**2 
definite_integral = sp.integrate(f,(x,0,2))
indefinite_integral = sp.integrate(f,x)
print("Definite Integral:",definite_integral)
print("Indefinite Integral:",indefinite_integral)


# define a function
x = sp.Symbol('x')
f = sp.exp(-x)

# compute indefinite integral
indefinite_integral = sp.integrate(f,x)
print("Indefinite Integral:",indefinite_integral)

# compute definite integral
definite_integral = sp.integrate(f,(x,0, sp.oo))
print("Definite Integral:",definite_integral)

import numpy as np 

# generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100 , 1)

# add bias term to x 
X_b = np.c_[np.ones((100,1),X)]

# SGD imp
def stochastic_gradient_descent(X, y, theta, learning_rate, n_epocs):
    m = len(y)
    for epoc in range(n_epocs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X[random_index:random_index+1]
            yi = y[random_index:random_index+1]
            gradients = 2*xi.T @ (xi @ theta - yi)
            theta -= learning_rate * gradients
    
    return theta


# initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.01
n_epocs = 50 

# perform SGD 
theta_opt = stochastic_gradient_descent(X_b, y, theta, learning_rate, n_epocs)
print("optimized parameters",theta_opt)
