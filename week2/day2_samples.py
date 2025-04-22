import numpy as np 

# DETERMINANT
A = np.array([[2,3],[1,4]])

# FORMULA FOR 2X2 det([a b]  = ad-bc
#                     [c d])

determinant = np.linalg.det(A)
print("Determinant: ",determinant)

# INVERSE
# ONLY IF DET(A) != 0
# FORMULA FOR 2X2 2X2 MATRIX
# A^-1 = 1/det(A) [[d,-b],[-c,a]]
inverse = np.linalg.inv(A)
print("Inverse of A: \n",inverse)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("eigenval \n",eigenvalues)
print("eigenvec \n",eigenvectors)

B = np.array([[4,2],[1,1]])
eigval,eigvec = np.linalg.eig(B)

# Matrix decomposition
U, S, Vt = np.linalg.svd(A) 

# reconstruct
Sigma = np.zeros((2,2))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
