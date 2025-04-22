import numpy as np 

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Addition: \n",A+B)
print("Subs: \n",A-B) 

C = 2 * A
print("Scalar multp: \n",C)

# matrix multiplication
# num of colms of 1st matrix must be equal to num of colms of 2nd
result = np.dot(A,B) 
print("matrix multip \n",result)


# diagonal 1
# I * A = A
I = np.eye(3)
print("Identity matrix \n",I)

Z = np.zeros((2,3))
print("Zero matrix \n",Z)

# diagonal matrix
D = np.diag([1,2,3])

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
v = np.array([1,0,-1])
result = np.dot(M,v)
