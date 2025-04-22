# DERIVATIVES
import sympy as sp 

x = sp.Symbol('x')
f = x**2
derivative = sp.diff(f,x)
print("derivative: ",derivative)

# gradient
x, y = sp.symbols('x y')
f = x**2 + y**2
grad_x = sp.diff(f,x)
grad_y = sp.diff(f,y)


# define a function
x = sp.Symbol('x')
f = x**3 - 5*x + 7

# compute derivative
derivative = sp.diff(f,x)
print("Function: ",f)
print("Derivative " ,derivative)

# define a multivariable function
x,y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y

# compute partial derivatives
grad_x = sp.diff(f,x)
grad_y = sp.diff(f,y)
print("Gradients:")
print("Grad x:",grad_x)
print("Grad y:",grad_y)

import numpy as np 
#define the gradient descent function
def gradient_descent(X,y,theta,learning_rate,iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X,theta)
        errors = predictions - y 
        gradients = (1/m) * np.dot(X.T,errors)
        theta -= learning_rate * gradients
    return theta

# sample data
X = np.array([[1,1],[1,2],[1,3]])
y = np.array([2,2.5,3.5])
theta = np.array([0.1,0.1])
learning_rate = 0.1
iterations = 1000

#perform gradient descent
optimized_theta = gradient_descent(X,y,theta,learning_rate,iterations)
