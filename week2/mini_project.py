import numpy as np 
# task1: implement the mathematical formula for linear regression

# generate synthetic data
np.random.seed(42)
X = 2*np.random.rand(100,1)
y = 4+3*X+np.random.randn(100,1)

# add bias term to feature matrix
X_b = np.c_[np.ones((100,1)),X]

# initialze parameters

theta = np.random.randn(2,1)
learning_rate = 0.1
iterations = 1000

def predict(X,theta):
    return np.dot(X, theta)

# task2: use gradient descent to optimize the model parameters
def gradient_descent(X,y,theta,learning_rate,iterations):
    m = len(y)
    for _ in range(iterations):
        gradients = (1/m) * np.dot(X.T,(np.dot(X,theta)- y))
        theta -= learning_rate * gradients
    return theta

# task3: calculate evaluation metrics

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def r_squared(y_true,y_pred):
    ss_res = np.sum((y_true-y_pred)**2)
    ss_tot = np.sum((y_true-np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)

# perform gradient descent
theta_optimized = gradient_descent(X_b,y,theta,learning_rate,iterations)

# predictions and evaluations
y_pred = predict(X_b,theta_optimized)
mse = mean_squared_error(y,y_pred)
r2 = r_squared(y,y_pred)

print("optimized parameters (theta):",theta_optimized)
print("mse :",mse)
print("r2 :",r2)
